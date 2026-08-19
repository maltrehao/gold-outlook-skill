#!/usr/bin/env python3
"""Aggregate qualitative gold signals without double-counting indicator families."""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path
from typing import Any


HORIZONS = ("short", "medium", "long")
FAMILY_WEIGHTS = {
    "short": {
        "opportunity_cost": 0.30,
        "usd_liquidity": 0.25,
        "fiscal_credibility": 0.05,
        "risk_official_demand": 0.15,
        "cross_asset_positioning": 0.25,
    },
    "medium": {
        "opportunity_cost": 0.35,
        "usd_liquidity": 0.25,
        "fiscal_credibility": 0.20,
        "risk_official_demand": 0.10,
        "cross_asset_positioning": 0.10,
    },
    "long": {
        "opportunity_cost": 0.20,
        "usd_liquidity": 0.10,
        "fiscal_credibility": 0.45,
        "risk_official_demand": 0.20,
        "cross_asset_positioning": 0.05,
    },
}


class InputError(ValueError):
    pass


def _number_for_horizon(value: Any, horizon: str, field: str) -> float | None:
    if isinstance(value, dict):
        value = value.get(horizon)
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise InputError(f"{field} must be numeric or a horizon mapping")
    return float(value)


def _label(score: float) -> str:
    if score >= 0.80:
        return "bullish"
    if score >= 0.25:
        return "mildly bullish"
    if score > -0.25:
        return "neutral/mixed"
    if score > -0.80:
        return "mildly bearish"
    return "bearish"


def _coverage_label(coverage: float) -> str:
    if coverage < 0.60:
        return "provisional"
    if coverage < 0.80:
        return "usable with gaps"
    return "broad evidence"


def _validate_signal(signal: Any, index: int) -> dict[str, Any]:
    if not isinstance(signal, dict):
        raise InputError(f"signals[{index}] must be an object")
    signal_id = signal.get("id")
    family = signal.get("family")
    if not isinstance(signal_id, str) or not signal_id.strip():
        raise InputError(f"signals[{index}].id must be a non-empty string")
    allowed_families = set(FAMILY_WEIGHTS["short"])
    if family not in allowed_families:
        raise InputError(
            f"signals[{index}].family must be one of {sorted(allowed_families)}"
        )
    if "impact" not in signal:
        raise InputError(f"signals[{index}].impact is required")
    if "confidence" not in signal:
        raise InputError(f"signals[{index}].confidence is required")
    scoped = signal.get("horizons", list(HORIZONS))
    if not isinstance(scoped, list) or not scoped:
        raise InputError(f"signals[{index}].horizons must be a non-empty list")
    unknown = set(scoped) - set(HORIZONS)
    if unknown:
        raise InputError(f"signals[{index}] has unknown horizons: {sorted(unknown)}")
    return signal


def score_payload(payload: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(payload, dict):
        raise InputError("input root must be an object")
    raw_signals = payload.get("signals")
    if not isinstance(raw_signals, list) or not raw_signals:
        raise InputError("signals must be a non-empty list")
    signals = [_validate_signal(item, i) for i, item in enumerate(raw_signals)]

    result: dict[str, Any] = {
        "as_of": payload.get("as_of"),
        "instrument": payload.get("instrument", "USD gold"),
        "method": "family-balanced qualitative score; not a price forecast",
        "horizons": {},
    }

    for horizon in HORIZONS:
        family_details: dict[str, Any] = {}
        for family in FAMILY_WEIGHTS[horizon]:
            members = []
            for signal in signals:
                if signal["family"] != family or horizon not in signal.get(
                    "horizons", HORIZONS
                ):
                    continue
                impact = _number_for_horizon(signal["impact"], horizon, "impact")
                confidence = _number_for_horizon(
                    signal["confidence"], horizon, "confidence"
                )
                if impact is None or confidence is None:
                    continue
                if not -2 <= impact <= 2:
                    raise InputError(f"{signal['id']} impact must be in [-2, 2]")
                if not 0 <= confidence <= 1:
                    raise InputError(f"{signal['id']} confidence must be in [0, 1]")
                if confidence == 0:
                    continue
                members.append(
                    {
                        "id": signal["id"],
                        "impact": impact,
                        "confidence": confidence,
                        "observation": signal.get("observation", ""),
                        "as_of": signal.get("as_of"),
                        "source": signal.get("source", ""),
                    }
                )
            if members:
                confidence_sum = sum(x["confidence"] for x in members)
                family_score = sum(
                    x["impact"] * x["confidence"] for x in members
                ) / confidence_sum
                family_confidence = confidence_sum / len(members)
                family_details[family] = {
                    "score": round(family_score, 4),
                    "confidence": round(family_confidence, 4),
                    "configured_weight": FAMILY_WEIGHTS[horizon][family],
                    "signals": members,
                }

        coverage = sum(
            FAMILY_WEIGHTS[horizon][family] for family in family_details
        )
        if not family_details:
            result["horizons"][horizon] = {
                "score": None,
                "label": "insufficient evidence",
                "coverage": 0.0,
                "coverage_label": "provisional",
                "evidence_confidence": 0.0,
                "conflict_index": None,
                "families": {},
                "missing_families": list(FAMILY_WEIGHTS[horizon]),
            }
            continue

        normalized = {
            family: FAMILY_WEIGHTS[horizon][family] / coverage
            for family in family_details
        }
        score = sum(
            normalized[family] * detail["score"]
            for family, detail in family_details.items()
        )
        evidence_confidence = sum(
            normalized[family] * detail["confidence"]
            for family, detail in family_details.items()
        )
        conflict_index = math.sqrt(
            sum(
                normalized[family] * (detail["score"] - score) ** 2
                for family, detail in family_details.items()
            )
        )
        result["horizons"][horizon] = {
            "score": round(score, 4),
            "label": _label(score),
            "coverage": round(coverage, 4),
            "coverage_label": _coverage_label(coverage),
            "evidence_confidence": round(evidence_confidence, 4),
            "conflict_index": round(conflict_index, 4),
            "families": family_details,
            "missing_families": [
                family
                for family in FAMILY_WEIGHTS[horizon]
                if family not in family_details
            ],
        }
    return result


def as_markdown(result: dict[str, Any]) -> str:
    lines = [
        "# Gold Outlook Score",
        "",
        f"As of: {result.get('as_of') or 'not supplied'}  ",
        f"Instrument: {result['instrument']}  ",
        "Method: family-balanced qualitative score; not a price target.",
        "",
        "| Horizon | Score | Label | Coverage | Evidence confidence | Conflict index |",
        "| --- | ---: | --- | ---: | ---: | ---: |",
    ]
    for horizon in HORIZONS:
        row = result["horizons"][horizon]
        score = "n/a" if row["score"] is None else f"{row['score']:.2f}"
        conflict = (
            "n/a"
            if row["conflict_index"] is None
            else f"{row['conflict_index']:.2f}"
        )
        lines.append(
            f"| {horizon} | {score} | {row['label']} | "
            f"{row['coverage']:.0%} ({row['coverage_label']}) | "
            f"{row['evidence_confidence']:.0%} | {conflict} |"
        )

    for horizon in HORIZONS:
        row = result["horizons"][horizon]
        lines.extend(["", f"## {horizon.title()} family scores", ""])
        if not row["families"]:
            lines.append("Insufficient evidence.")
            continue
        lines.extend(
            [
                "| Family | Score | Confidence | Configured weight | Signals |",
                "| --- | ---: | ---: | ---: | --- |",
            ]
        )
        for family, detail in row["families"].items():
            ids = ", ".join(x["id"] for x in detail["signals"])
            lines.append(
                f"| {family} | {detail['score']:.2f} | "
                f"{detail['confidence']:.0%} | {detail['configured_weight']:.0%} | {ids} |"
            )
        if row["missing_families"]:
            lines.extend(
                ["", "Missing families: " + ", ".join(row["missing_families"]) + "."]
            )
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="JSON file containing signal observations")
    parser.add_argument(
        "--format", choices=("json", "markdown"), default="json", dest="output_format"
    )
    args = parser.parse_args()
    try:
        with args.input.open("r", encoding="utf-8") as handle:
            payload = json.load(handle)
        result = score_payload(payload)
    except (OSError, json.JSONDecodeError, InputError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    if args.output_format == "markdown":
        print(as_markdown(result), end="")
    else:
        json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

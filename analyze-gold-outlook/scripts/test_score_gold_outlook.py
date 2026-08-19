#!/usr/bin/env python3
"""Small standard-library regression test for score_gold_outlook.py."""

import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("scorer", HERE / "score_gold_outlook.py")
assert SPEC and SPEC.loader
SCORER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SCORER)


def main() -> None:
    payload = json.loads((HERE / "example_signals.json").read_text(encoding="utf-8"))
    result = SCORER.score_payload(payload)
    assert set(result["horizons"]) == {"short", "medium", "long"}
    assert result["horizons"]["short"]["coverage"] == 1.0
    assert result["horizons"]["medium"]["coverage"] == 1.0
    assert result["horizons"]["long"]["coverage"] == 1.0
    assert result["horizons"]["long"]["score"] > result["horizons"]["short"]["score"]
    markdown = SCORER.as_markdown(result)
    assert "Gold Outlook Score" in markdown
    assert "family-balanced" in markdown
    print("ok")


if __name__ == "__main__":
    main()

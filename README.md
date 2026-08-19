# Gold Outlook Skill｜黄金多周期研判

一个面向 ChatGPT/Codex 类智能体的开源黄金研究 Skill。它不依赖“某个指标永远有效”的假设，而是把黄金拆成机会成本、美元与流动性、财政信用、避险与官方需求、跨资产与仓位五条因果链，分别形成短期、中期和长期判断。

核心特色是把 **A 股黄金股** 作为有条件的前瞻信号，而不是机械认定“黄金股上涨必然领先金价”；同时把 **金银比** 与黄金、白银的绝对价格方向联合解释，避免把相对强弱错误地当成绝对看多信号。

## 能解决什么问题

- 研判美元金、人民币金、黄金 ETF 和黄金股的短中长期走势。
- 解释美联储政策、TIPS 实际利率、美元指数、美元流动性与美债供给如何传导至黄金。
- 判断 A 股黄金股究竟在领先金价，还是仅反映人民币贬值、成本变化、股市 Beta 或公司事件。
- 结合金银比、ETF/CFTC 仓位、矿业股广度等信号，检查行情是否拥挤或得到跨资产确认。
- 输出基准、牛市和熊市情景，以及可观测的确认条件和失效条件。

## 框架概览

| 因子家族 | 核心变量 | 主要期限 | 在框架中的作用 |
| --- | --- | --- | --- |
| 机会成本 | 5Y/10Y TIPS、Fed 路径、实际利率曲线 | 短期/中期 | 决定持有无息黄金的相对成本 |
| 美元与流动性 | DXY、银行准备金、TGA、ON RRP、美债发行结构 | 短期/中期 | 决定美元计价压力和边际资金条件 |
| 财政与信用 | 财政赤字、利息支出、期限溢价、货币财政协调 | 中期/长期 | 决定黄金的货币信用溢价 |
| 避险与官方需求 | 地缘风险、央行购金、储备多元化 | 中期/长期 | 决定结构性需求与尾部风险溢价 |
| 跨资产与仓位 | 金银比、ETF/CFTC、A 股黄金股 | 短期/中期 | 用于择时、拥挤度与前瞻确认 |

最终逻辑不是“五项投票”，而是：**冲击 → 增长/通胀预期 → Fed 与期限溢价 → 实际利率 → 美元/流动性 → 仓位和资金流 → 黄金**。同一事件在不同期限可以产生相反影响，例如大量附息美债发行短期可能推高实际利率并压制黄金，长期却可能通过财政信用溢价支持黄金。

## 目录结构

```text
analyze-gold-outlook/
├── SKILL.md
├── agents/openai.yaml
├── assets/icon.svg
├── references/
│   ├── framework.md
│   ├── indicators.md
│   ├── a-share-gold-equities.md
│   ├── scoring.md
│   ├── data-sources.md
│   └── output-template.md
└── scripts/
    ├── score_gold_outlook.py
    ├── example_signals.json
    └── test_score_gold_outlook.py
```

## 安装

克隆仓库后，将 `analyze-gold-outlook` 整个目录复制到支持 Skills 的智能体技能目录中。不同客户端的技能目录位置可能不同；核心要求是保留 `SKILL.md`、`references`、`scripts`、`agents` 和 `assets` 的相对结构。

```bash
git clone https://github.com/maltrehao/gold-outlook-skill.git
cp -R gold-outlook-skill/analyze-gold-outlook <your-skills-directory>/
```

安装后可以直接使用类似请求：

```text
使用 $analyze-gold-outlook 分析当前黄金未来一个月、一个季度和两年的走势，
重点判断 A 股黄金股是否领先，并给出基准、牛市、熊市情景和失效条件。
```

## Agent 调用说明

仓库根目录提供了 [AGENTS.md](AGENTS.md)，用于告诉 Codex、Claude Code 等代码 Agent 如何识别、加载和执行本 Skill。Agent 进入仓库后应先完整读取 `analyze-gold-outlook/SKILL.md`，再根据问题按需加载参考文件，而不是一次性把所有资料放入上下文。

支持显式 Skill 调用的客户端可以直接使用：

```text
使用 $analyze-gold-outlook 分析当前美元金和人民币金的短期、中期和长期走势，
判断 A 股黄金股是否构成前瞻信号，并给出验证条件和失效条件。
```

不支持 `$skill-name` 语法的 Agent，可以使用路径调用：

```text
请先读取并严格遵循 analyze-gold-outlook/SKILL.md，
然后分析当前黄金未来一个月、一个季度和两年的走势。
```

## 可审计评分器

评分器接受人工或智能体基于证据映射后的 `impact`（-2 到 +2）和 `confidence`（0 到 1）。它先在因子家族内部聚合，再按期限加权，防止多个高度相关的利率指标被重复计算。

```bash
python3 analyze-gold-outlook/scripts/score_gold_outlook.py \
  analyze-gold-outlook/scripts/example_signals.json \
  --format markdown
```

示例数据全部标记为 synthetic，仅用于演示输入结构，不能作为真实市场观点。评分器是研究审计工具，不是训练完成的预测模型，也不会自动生成目标价。

## 验证

项目仅使用 Python 标准库：

```bash
python3 -m py_compile analyze-gold-outlook/scripts/score_gold_outlook.py
python3 analyze-gold-outlook/scripts/test_score_gold_outlook.py
```

## 研究边界

黄金的驱动关系会随宏观制度、市场拥挤度和流动性状态变化。本 Skill 强制区分事实、推断和预测，要求对实时信息使用最新的一手来源，并明确观察日期、发布时间、频率与修订风险。任何输出都应被理解为研究框架和情景分析，而非收益承诺或个性化投资建议。

## License

[MIT](LICENSE)

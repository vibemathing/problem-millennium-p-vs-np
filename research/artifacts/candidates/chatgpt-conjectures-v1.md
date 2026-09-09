# Candidate-only Eight-Category Conjecture Map (ChatGPT export)

- Repository: vibemathing/problem-millennium-p-vs-np
- Problem: problem:millennium-p-vs-np
- Source chat content SHA-256: `32c5a617d459a1227280e3f887e2ea3996d206c422eb7d86aa4c37a6ca6e8947`
- Status: candidate_only; statement_faithfulness pending; prior-art review pending; independent verification pending
- Transport classification: computation (bounded classification/catalog audit). This file claims no proof, counterexample, Evidence, Result, or Solution.
- Excerp from CONJECTURE_CATALOG.md section below (verbatim).

输入：`httpsgithub.comvibemathingproblem-millennium-p-vs-np-提出猜想 !-20260909-1743.md`
1. `PVSNP-E` 存在：存在小阈值 `mu` 使 `MCSP[2^(mu n)]` 不属于指定单带模型的近线性时间类。
2. `PVSNP-U` 全称：对所有 `mu>0` 都有相应 MCSP 超线性下界；强版本，必须标明模型。
3. `PVSNP-R` 刚性：若较大阈值 MCSP 困难，则较小阈值也困难；这是最值得先攻击的阈值向下传递候选。
4. `PVSNP-Q` 对应：`P=NP` 当且仅当 `MCSP` 属于 `P`；左到右显然，右到左是开放候选，不能写成已知等价。
5. `PVSNP-K` 分类：困难阈值集合 `H={mu:H(mu)}` 是单区间，存在临界 `mu_c`；要做 oracle/relativization 压力测试。
6. `PVSNP-B` 界：hardness-magnification 所需的小阈值 `mu0` 上存在 `N^1.01` 单带下界；须锁定具体定理的模型和常数。
7. `PVSNP-A` 渐近：时间指数曲线 `tau(mu)` 满足 `liminf_{mu->0+} tau(mu)>1`；这是候选研究对象，不是现有定理。
8. `PVSNP-D` 复杂度：受限 MCSP 是 NP-complete，或至少存在固定模型下的统一判定/归约复杂度界；需先查最新文献。
首选后续路线：先冻结 MCSP 变体、输入长度 `N=2^n`、单带模型和 `mu0` 来源；聊天中把 2025/2026 结果作为未核验来源线索。

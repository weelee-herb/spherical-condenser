# Changelog

## v1.0.0 (2026-10-30)

- 首版 pack：8 个可发现入口（7 晋级 Skill + 1 来源路由入口），13 条验证能力。
- 三重验证 55 候选 → 13 verified / 34 reference / 2 needs_review / 6 rejected。
- 触发压力测试 72/72（独立盲测 + 回归；诱饵容错 0）；修复 5 条技能 trigger 歧义 + 1 条测试设计（留审计）。
- 编译硬门 validate_skill_pack 0 errors / 0 warnings。
- 已知缺口：p08/p11 needs_review 未进正片；阶段 4 输出侧评测未实测。

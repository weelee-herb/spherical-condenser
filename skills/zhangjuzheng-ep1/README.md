# 大明脊梁张居正 · 第 1 集蒸馏包（zhangjuzheng-ep1 pack）

> Distilled, verified agent skills from 郦波《大明脊梁张居正》(Episode 1, CCTV 百家讲坛).

## 这是什么

用 cangjie-skill 五阶段流水线把一期 27 分钟讲座蒸馏成 **8 个可发现入口**：

- 7 个晋级 Skill：education-four-factors / before-after-three-line-eval / age-adapted-teaching-material / suspense-hook-delayed-reveal / key-person-selection-4-steps / interest-duty-priority-persuasion / teacher-student-feedback-loop
- 1 个来源路由入口：zhangjuzheng-ep1-source（6 个能力卡 + 案例/反例/术语参考）

## 什么情况用哪个技能（速查表）

| 你的处境 | 用哪个 |
|---|---|
| 孩子教育出问题，或比较两套选校/选课方案 | education-four-factors |
| 评估一次改版/改革有没有效果（含数据） | before-after-three-line-eval |
| 给低龄/小白把难概念讲明白、判断教学材料 | age-adapted-teaching-material |
| 连载内容要设悬念钩子、排期 | suspense-hook-delayed-reveal |
| 有中间人推荐老师/合伙人，拿不准要不要录用 | key-person-selection-4-steps |
| 劝人收束影响正事的爱好，怕吵起来 | interest-duty-priority-persuasion |
| 给下属/学生提改进建议，怕打击积极性 | teacher-student-feedback-loop |
| 以上之外的讲座相关问法（四=零、惩教升级链、人物评价、年号换算…） | zhangjuzheng-ep1-source |

## 质量证据

- 三重验证：55 候选 → 13 verified / 34 reference / 2 needs_review / 6 rejected（逐条留依据）
- 触发压力测试：72 条盲测 **72/72**（独立 sub-agent 盲测 + 回归，诱饵容错 0）
- 编译硬门：validate_skill_pack 0 errors / 0 warnings
- 输出侧评测：2 个代表任务 × 有无技能对照，结果见 `eval/output-results.md`（其余能力续测中）
- 缺口如实声明：p08/p11 needs_review（史料口径待考）

## 安装

把本目录下 **8 个 skill 目录**（不是本包目录本身）复制/链接到宿主的 skills 目录：

- Claude Code：`~/.claude/skills/<skill-name>/`（每个 skill 一个子目录）
- Codex：本机技能目录（如 `~/.agents/skills/` 或 `$CODEX_HOME/skills/`），同样每个 skill 一个子目录

例（Claude Code）：

```bash
cp -R skills/zhangjuzheng-ep1/* ~/.claude/skills/
```

8 个目录建议一起装：7 个晋级技能单独可触发，但正文里引用的能力卡（如四=零模型 f02、多源评估 f10）经 `zhangjuzheng-ep1-source` 路由入口到达；只装单个技能不会报错，但交叉引用会找不到对应卡。

## 引用如何自查

各技能 R 段的引文行号指向本机转写稿（因版权不随包分发）。为让「每条引用可核」不落空，本包附 `quotes-verification.json`：13 条能力卡的 71 段引文（≤150 字/段）全文与行号摘录，可据此逐字核对；如仍需完整转写稿，见 SOURCE-NOTICE.md。

## 许可与署名

- 代码与文本：MIT（见 LICENSE）
- 内容来源与引用边界：见 SOURCE-NOTICE.md

## 路线图

- [ ] output_cases 补齐其余 11 个能力
- [ ] p08/p11 史料闭合后升级为 verified

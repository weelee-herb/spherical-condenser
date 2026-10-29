# 大明脊梁张居正 · 第 1 集蒸馏包（zhangjuzheng-ep1 pack）

> Distilled, verified agent skills from 郦波《大明脊梁张居正》(Episode 1, CCTV 百家讲坛).

## 这是什么

用 cangjie-skill 五阶段流水线把一期 27 分钟讲座蒸馏成 **8 个可发现入口**：

- 7 个晋级 Skill：education-four-factors / before-after-three-line-eval / age-adapted-teaching-material / suspense-hook-delayed-reveal / key-person-selection-4-steps / interest-duty-priority-persuasion / teacher-student-feedback-loop
- 1 个来源路由入口：zhangjuzheng-ep1-source（6 个能力卡 + 案例/反例/术语参考）

## 质量证据

- 三重验证：55 候选 → 13 verified / 34 reference / 2 needs_review / 6 rejected（逐条留依据）
- 触发压力测试：72 条盲测 **72/72**（独立 sub-agent 盲测 + 回归，诱饵容错 0）
- 编译硬门：validate_skill_pack 0 errors / 0 warnings
- 缺口如实声明：p08/p11 needs_review；阶段 4 输出侧评测（output_cases）未实测

## 安装

把本目录下各 skill 目录复制/链接到宿主 skills 目录（如 `~/.claude/skills/`、Codex 技能库），或直接引用本目录路径。

## 许可与署名

- 代码与文本：MIT（见 LICENSE）
- 内容来源与引用边界：见 SOURCE-NOTICE.md

## 路线图

- [ ] output_cases 实际输出评测（阶段 4 输出侧）
- [ ] p08/p11 史料闭合后升级为 verified
- [ ] 英文 description 双语化

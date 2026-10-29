# 球形冷凝管 · Spherical Condenser

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
  <img src="https://img.shields.io/badge/PRs-welcome-brightgreen" alt="PRs welcome">
  <img src="https://img.shields.io/badge/blind%20tests-72%2F72-blue" alt="Blind tests 72/72">
</p>

> 把高质量内容蒸馏成**可验证的 Agent 技能**。
> Distilling high-quality content into *verifiable* agent skills.

冷凝管回流的是纯净的蒸馏液——这个仓库做的事也一样：从讲座、书籍里提炼方法论，经三重验证、触发盲测与格式硬门，只留下能被可靠调用的技能。**本仓库只开源蒸馏产物**，不包含任何私有工作流。

## 内容

### `skills/zhangjuzheng-ep1/` — 大明脊梁张居正·第 1 集蒸馏包

- 8 个可发现入口：7 个晋级 Skill + 1 个来源路由入口（13 条验证能力）
- 质量证据：三重验证 55 候选 → 13 verified；触发盲测 **72/72**（诱饵容错 0）；格式硬门 0 error
- 盲测资产开源在 `eval/`：`test-prompts.json`（72 用例）、`output-cases.json` 与结果报告
- 内容来源与引用边界：见该包 `SOURCE-NOTICE.md`

## 安装

把技能目录复制/链接到宿主 skills 目录（Claude Code、Codex 等）即可。

## 质量红线

1. 每条事实必须有来源可追溯；无一手来源不进正片。
2. 触发词必须经盲测（正例 + 诱饵 + 边界），诱饵容错 0。
3. 发布前跑本仓库 `tools/validate_skills.py`。

## 许可与署名

- 代码与文本：MIT（见 LICENSE）
- 单个技能包可另有来源声明（见各包 SOURCE-NOTICE.md），使用时请逐包核对
- 作者：湖东野

## 路线图

- [ ] 阶段 4 输出侧评测补齐全部能力并公开结果
- [ ] p08/p11 史料缺口闭合后升级为 verified
- [ ] 更多讲座/书籍的蒸馏包（同一流水线复跑）

#!/usr/bin/env python3
"""技能包格式校验（本仓库自有轻量实现）：每个技能目录必须有 SKILL.md，
frontmatter 含 name/description 且 name 与目录名一致；description 非空。
用法：python3 tools/validate_skills.py [root]
"""
import re
import sys
from pathlib import Path

def check_skill(path: Path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return "缺少 frontmatter"
    end = text.find("\n---", 3)
    if end < 0:
        return "frontmatter 未闭合"
    fm = text[3:end]
    name = re.search(r"^name:\s*(\S+)", fm, re.M)
    desc_m = re.search(r"^description:\s*(.*)$", fm, re.M)
    if not name:
        return "缺少 name"
    if name.group(1) != path.parent.name:
        return f"name {name.group(1)} 与目录名 {path.parent.name} 不一致"
    if not desc_m:
        return "缺少 description"
    if desc_m.group(1) == "|":
        # block scalar：取块内第一个非空行
        body = fm[desc_m.end():]
        nonempty = next((l.strip() for l in body.splitlines() if l.strip()), "")
        if not nonempty:
            return "description 为空"
    elif not desc_m.group(1).strip():
        return "description 为空"
    return None

def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    errors = 0
    total = 0
    for sk in sorted(root.rglob("SKILL.md")):
        if ".git" in sk.parts:
            continue
        total += 1
        err = check_skill(sk)
        if err:
            errors += 1
            print(f"FAIL {sk.relative_to(root)}: {err}")
    print(f"validate_skills: {total} SKILL.md, {errors} errors")
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())

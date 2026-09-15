#!/usr/bin/env python3
"""Regenerate README.md and README_zh.md from articles.yaml.

Usage:
    python scripts/gen_readmes.py           # write both READMEs
    python scripts/gen_readmes.py --check   # verify READMEs are up to date (exit 1 if stale)

Single source of truth: articles.yaml at the repo root. Editing the READMEs
directly is discouraged - change articles.yaml and regenerate instead.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "articles.yaml"
README_EN = ROOT / "README.md"
README_ZH = ROOT / "README_zh.md"

ROMAN = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
CN_NUM = ["一", "二", "三", "四", "五", "六", "七", "八", "九", "十"]

SKILLS_DIR = ROOT / ".opencode" / "skills"
CLAWHUB_SKILL_URL = "https://clawhub.ai/j3ffyang/skills/{slug}"

SKILLS_TITLE_EN = "Published Skills on ClawHub"
SKILLS_TITLE_ZH = "已发布技能（ClawHub）"
SKILLS_NOTE_EN = (
    "Developed in this repo and auto-published to "
    "[ClawHub](https://clawhub.ai/j3ffyang) on every push."
)
SKILLS_NOTE_ZH = (
    "在本仓库中开发，每次推送时自动发布到 "
    "[ClawHub](https://clawhub.ai/j3ffyang) 上。"
)

INTRO_EN = """\
# ai_thoughts

[中文版](README_zh.md)

A bilingual (English · 中文) collection of articles and essays spanning three domains: **technology** (hands-on experience with OpenClaw 🦞 and Hermes Agent ⚕, privacy, knowledge management), **history**, and **culture & philosophy** (motorcycle culture, how different cultures face death, the "unknown unknowns" of knowledge). This page indexes the English articles; Chinese-language articles (including most culture posts) are listed in the [中文版](README_zh.md).

Images for each article live in the [`imgs/`](imgs/) subdirectory and follow the same `YYMMDD-slug` naming convention as the articles themselves.

Custom OpenCode skills developed here auto-publish to [ClawHub](https://clawhub.ai/j3ffyang) — the Published Skills table below lists each one.

---
"""

INTRO_ZH = """\
# ai_thoughts

[English](README.md)

中英双语（English · 中文）文章与随笔合集，涵盖三大领域：**技术**（OpenClaw 🦞 与 Hermes Agent ⚕ 的实战体验、隐私、知识管理）、**历史**、以及**文化与哲思**（摩托车文化、不同文化如何面对死亡、"未知的未知"）。内容涵盖实操指南（自定义技能开发、自托管部署加固），以及更具个人色彩的写作（个人创业、骑行文化）。

每篇文章的配图存放于 [`imgs/`](imgs/) 子目录，沿用与文章相同的 `YYMMDD-slug` 命名规范。

本仓库自研的 OpenCode 技能会在每次推送时自动发布到 [ClawHub](https://clawhub.ai/j3ffyang)——下方"已发布技能"表格逐项列出。

---
"""

FOOTER_EN = """
---

> **Maintaining this index:** edit [`articles.yaml`](articles.yaml), then run `python scripts/gen_readmes.py` to regenerate `README.md` and [`README_zh.md`](README_zh.md).
> The Published Skills table is auto-derived from each `.opencode/skills/*/SKILL.md` frontmatter, linking to its ClawHub page. Article sections are ordered by newest post; drafts stay last.
"""

FOOTER_ZH = """
---

> **维护说明：** 编辑 [`articles.yaml`](articles.yaml)，然后运行 `python scripts/gen_readmes.py` 重新生成 `README.md` 与 [`README_zh.md`](README.md)。
> "已发布技能"表格根据各 `.opencode/skills/*/SKILL.md` 的 frontmatter 自动生成，并链接到对应 ClawHub 页面。文章分区按最新文章排序，草稿固定在末尾。
"""

DRAFTS_INTRO_EN = (
    "Earlier versions of articles are kept alongside their final versions so each "
    "piece shows the evolution from brainstorming doc to finished post. These are "
    "the drafts that became (or are becoming) the articles above."
)
DRAFTS_INTRO_ZH = (
    "旧版文章与其最终版并存，是为了让每一篇都展示从头脑风暴文档到成稿的演变过程。"
    "以下是促成（或正在促成）上述文章的草稿。"
)


def load_manifest() -> dict:
    with MANIFEST.open(encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    return data


def validate(data: dict) -> None:
    errors: list[str] = []
    sections = {s["id"]: s for s in data["sections"]}
    for i, row in enumerate(data["rows"]):
        if row["section"] not in sections:
            errors.append(f"row {i}: unknown section '{row['section']}'")
        has_en = any(ln.get("lang") == "en" for ln in row["links"])
        has_zh = any(ln.get("lang") == "zh" for ln in row["links"])
        has_chn_file = any(
            (ROOT / (ln["path"][:-3] + "-chn.md")).is_file()
            for ln in row["links"]
            if ln.get("lang") == "en"
        )
        if (has_zh or has_chn_file) and (not row.get("desc_zh") or not row["desc_zh"]):
            errors.append(f"row {i}: missing desc_zh (a -chn.md exists for this article)")
        if has_en and (not row.get("desc_en") or not row["desc_en"]):
            errors.append(f"row {i}: has en link but missing desc_en")
        for ln in row["links"]:
            if not (ROOT / ln["path"]).is_file():
                errors.append(f"row {i}: link file does not exist: {ln['path']}")
    if errors:
        for e in errors:
            print(f"error: {e}", file=sys.stderr)
        sys.exit(1)


def render_links(links: list[dict], lang: str) -> str:
    selected = [ln for ln in links if ln.get("lang") == lang] if lang == "en" else links
    if lang == "zh":
        parts = [f"[{ln.get('label_zh') or ln['label']}]({ln['path']})" for ln in selected]
    else:
        parts = [f"[{ln['label']}]({ln['path']})" for ln in selected]
    return " · ".join(parts)


def row_date(row: dict) -> str:
    for ln in row["links"]:
        m = re.match(r"^(\d{6})", Path(ln["path"]).name)
        if m:
            return m.group(1)
    return "000000"


def ordered_sections(data: dict, sections: list[dict]) -> list[dict]:
    rows = data["rows"]
    arts = [s for s in sections if s["id"] != "drafts" and any(r["section"] == s["id"] for r in rows)]
    drafts = [s for s in sections if s["id"] == "drafts"]
    arts.sort(key=lambda s: max(row_date(r) for r in rows if r["section"] == s["id"]), reverse=True)
    return arts + drafts


def cell(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def skill_mtime(slug: str) -> int:
    try:
        proc = subprocess.run(
            ["git", "log", "-1", "--format=%ct", "--", f".opencode/skills/{slug}"],
            capture_output=True, text=True, cwd=ROOT, timeout=10,
        )
        return int(proc.stdout.strip()) if proc.returncode == 0 and proc.stdout.strip() else 0
    except Exception:
        return 0


def load_skills() -> list[dict]:
    skills = []
    if not SKILLS_DIR.is_dir():
        return skills
    for folder in sorted(SKILLS_DIR.iterdir()):
        if not folder.is_dir():
            continue
        md = folder / "SKILL.md"
        if not md.is_file():
            continue
        text = md.read_text(encoding="utf-8")
        m = re.match(r"^---\s*\n(.*?)\n---", text, re.S)
        front = yaml.safe_load(m.group(1)) if m else {}
        front = front or {}
        skills.append(
            {
                "slug": folder.name,
                "name": front.get("name") or folder.name,
                "description": front.get("description") or "",
            }
        )
    skills.sort(key=lambda s: (-skill_mtime(s["slug"]), s["slug"]))
    return skills


def skills_block(is_zh: bool, num: int, skills: list[dict]) -> list[str]:
    title = SKILLS_TITLE_ZH if is_zh else SKILLS_TITLE_EN
    note = SKILLS_NOTE_ZH if is_zh else SKILLS_NOTE_EN
    heading = f"### {CN_NUM[num - 1]}、{title}" if is_zh else f"### {ROMAN[num - 1]}. {title}"
    header, sep = ("| 技能 | 简介 |", "|---|---|") if is_zh else ("| Skill | Description |", "|---|---|")
    out = ["", heading, "", note, "", header, sep]
    for s in skills:
        url = CLAWHUB_SKILL_URL.format(slug=s["slug"])
        out.append(f"| [{cell(s['name'])}]({url}) | {cell(s['description'])} |")
    return out


def build(lang: str, data: dict, sections: list[dict], skills: list[dict]) -> str:
    rows = data["rows"]
    is_zh = lang == "zh"
    out: list[str] = [INTRO_ZH if is_zh else INTRO_EN, "## 目录" if is_zh else "## Contents"]

    num = 0
    for sec in ordered_sections(data, sections):
        if sec["id"] == "drafts":
            num += 1
            out.extend(skills_block(is_zh, num, skills))

        sec_rows = [r for r in rows if r["section"] == sec["id"]]
        sec_rows.sort(key=row_date, reverse=True)
        if not is_zh:
            sec_rows = [r for r in sec_rows if any(ln.get("lang") == "en" for ln in r["links"])]
        if not sec_rows:
            continue

        num += 1
        title = sec["title_zh"] if is_zh else sec["title_en"]
        heading = f"### {CN_NUM[num - 1]}、{title}" if is_zh else f"### {ROMAN[num - 1]}. {title}"
        out.append("")
        out.append(heading)
        out.append("")

        if sec["id"] == "drafts":
            out.append(DRAFTS_INTRO_ZH if is_zh else DRAFTS_INTRO_EN)
            out.append("")
            header, sep = ("| 草稿 | 说明 |", "|---|---|") if is_zh else ("| Draft | Notes |", "|---|---|")
        else:
            header, sep = ("| 文章 | 简介 |", "|---|---|") if is_zh else ("| Article | Description |", "|---|---|")
        out.append(header)
        out.append(sep)
        for r in sec_rows:
            links = render_links(r["links"], lang)
            desc = (r.get("desc_zh") or r["desc_en"]) if is_zh else r["desc_en"]
            out.append(f"| {links} | {desc} |")

    out.append(FOOTER_EN if lang == "en" else FOOTER_ZH)
    return "\n".join(out).lstrip("\n") + "\n"


def unlisted_warnings(data: dict) -> None:
    referenced = {ln["path"] for r in data["rows"] for ln in r["links"]}
    docs = sorted(p for p in (ROOT / "docs").glob("*.md"))
    missing = [str(p.relative_to(ROOT)) for p in docs if str(p.relative_to(ROOT)) not in referenced]
    if missing:
        print("warning: docs/*.md not listed in articles.yaml:")
        for m in missing:
            print(f"  - {m}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true", help="verify READMEs are up to date")
    args = ap.parse_args()

    data = load_manifest()
    validate(data)
    unlisted_warnings(data)
    sections = data["sections"]
    skills = load_skills()

    en = build("en", data, sections, skills)
    zh = build("zh", data, sections, skills)

    if args.check:
        ok = True
        for target, generated in ((README_EN, en), (README_ZH, zh)):
            current = target.read_text(encoding="utf-8") if target.exists() else None
            if current != generated:
                ok = False
                print(f"stale: {target.name} is out of date — run python scripts/gen_readmes.py")
        return 0 if ok else 1

    README_EN.write_text(en, encoding="utf-8")
    README_ZH.write_text(zh, encoding="utf-8")
    print(f"wrote {README_EN.name} ({len(en.splitlines())} lines)")
    print(f"wrote {README_ZH.name} ({len(zh.splitlines())} lines)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

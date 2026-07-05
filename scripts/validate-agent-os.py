#!/usr/bin/env python3
"""Valida a estrutura do Agent OS (root files, skills, memory, templates)."""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

REQUIRED_ROOT_FILES = [
    "AGENTS.md", "SOUL.md", "USER.md", "GOALS.md", "MAPA.md",
    "MEMORY.md", "TOOLS.md", "PROPAGATION.md", "HERMES.md",
    "agent-os.yaml", "README.md",
]

REQUIRED_MEMORY_FILES = ["decisions.md", "ideas.md", "lessons.md", "tasks.md"]

REQUIRED_TEMPLATES = ["SKILL-TEMPLATE.md", "ROOT-FILES-CHECKLIST.md"]


def check_root_files():
    errors = []
    for name in REQUIRED_ROOT_FILES:
        if not (REPO_ROOT / name).is_file():
            errors.append(f"Root file ausente: {name}")
    return errors


def check_skills():
    errors = []
    skills_dir = REPO_ROOT / "skills"
    if not skills_dir.is_dir():
        return ["Diretório skills/ ausente"]

    skill_mds = list(skills_dir.rglob("SKILL.md"))
    if not skill_mds:
        errors.append("Nenhum SKILL.md encontrado em skills/")

    for skill_md in skill_mds:
        rel = skill_md.relative_to(skills_dir)
        parts = rel.parts
        if len(parts) != 3:
            errors.append(f"Skill fora do formato skills/{{categoria}}/{{nome}}/SKILL.md: {rel}")
            continue
        content = skill_md.read_text(encoding="utf-8")
        if not content.startswith("---"):
            errors.append(f"Skill sem frontmatter: {rel}")
        elif "name:" not in content.split("---")[1] or "description:" not in content.split("---")[1]:
            errors.append(f"Skill sem name/description no frontmatter: {rel}")

    # sinalizar arquivos .md soltos fora do padrão SKILL.md
    for md in skills_dir.rglob("*.md"):
        if md.name != "SKILL.md":
            errors.append(f"Arquivo de skill fora do padrão (deveria ser SKILL.md): {md.relative_to(skills_dir)}")

    return errors


def check_memory():
    errors = []
    memory_dir = REPO_ROOT / "memory"
    if not memory_dir.is_dir():
        return ["Diretório memory/ ausente"]
    for name in REQUIRED_MEMORY_FILES:
        if not (memory_dir / name).is_file():
            errors.append(f"Arquivo de memory ausente: memory/{name}")
    return errors


def check_templates():
    errors = []
    templates_dir = REPO_ROOT / "templates"
    if not templates_dir.is_dir():
        return ["Diretório templates/ ausente"]
    for name in REQUIRED_TEMPLATES:
        if not (templates_dir / name).is_file():
            errors.append(f"Template ausente: templates/{name}")
    return errors


def check_scripts():
    errors = []
    scripts_dir = REPO_ROOT / "scripts"
    if not (scripts_dir / "sync.sh").is_file():
        errors.append("scripts/sync.sh ausente")
    if not (scripts_dir / "validate-agent-os.py").is_file():
        errors.append("scripts/validate-agent-os.py ausente")
    return errors


def main():
    all_errors = []
    all_errors += check_root_files()
    all_errors += check_skills()
    all_errors += check_memory()
    all_errors += check_templates()
    all_errors += check_scripts()

    if all_errors:
        print("❌ Estrutura do Agent OS com problemas:\n")
        for e in all_errors:
            print(f"  - {e}")
        sys.exit(1)

    print("✅ Estrutura do Agent OS válida.")
    sys.exit(0)


if __name__ == "__main__":
    main()

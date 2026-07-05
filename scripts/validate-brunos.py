#!/usr/bin/env python3
"""Valida a estrutura do BrunoOS (root files, projects, knowledge, templates, skills)."""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

REQUIRED_ROOT_FILES = [
    "README.md", "USER.md", "GOALS.md", "DECISION_RULES.md", "THINKING.md",
    "WORKFLOW.md", "WRITING_STYLE.md", "PROJECTS.md", "NOW.md", "IDEAS.md",
]

REQUIRED_PROJECTS = ["AventuFilm.md", "Ambialles.md"]

REQUIRED_TEMPLATES = ["PRD.md", "Proposal.md", "Meeting.md", "Decision.md", "Project.md", "Skill.md"]

REQUIRED_LOGS = ["decisions.md", "lessons.md"]


def check_root_files():
    errors = []
    for name in REQUIRED_ROOT_FILES:
        if not (REPO_ROOT / name).is_file():
            errors.append(f"Root file ausente: {name}")
    return errors


def check_projects():
    errors = []
    projects_dir = REPO_ROOT / "projects"
    if not projects_dir.is_dir():
        return ["Diretório projects/ ausente"]
    for name in REQUIRED_PROJECTS:
        if not (projects_dir / name).is_file():
            errors.append(f"Projeto ausente: projects/{name}")
    return errors


def check_knowledge():
    errors = []
    knowledge_dir = REPO_ROOT / "knowledge"
    if not knowledge_dir.is_dir():
        errors.append("Diretório knowledge/ ausente")
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


def check_skills():
    errors = []
    skills_dir = REPO_ROOT / "skills" / "ideation"
    if not skills_dir.is_dir():
        return ["Diretório skills/ideation/ ausente"]

    for skill_dir in sorted(p for p in skills_dir.iterdir() if p.is_dir()):
        readme = skill_dir / "README.md"
        workflow = skill_dir / "workflow.md"
        if not readme.is_file():
            errors.append(f"Skill sem README.md: {skill_dir.name}")
        elif not readme.read_text(encoding="utf-8").startswith("---"):
            errors.append(f"Skill sem frontmatter em README.md: {skill_dir.name}")
        if not workflow.is_file():
            errors.append(f"Skill sem workflow.md: {skill_dir.name}")
    return errors


def check_logs():
    errors = []
    logs_dir = REPO_ROOT / "logs"
    if not logs_dir.is_dir():
        return ["Diretório logs/ ausente"]
    for name in REQUIRED_LOGS:
        if not (logs_dir / name).is_file():
            errors.append(f"Log ausente: logs/{name}")
    return errors


def check_scripts():
    errors = []
    scripts_dir = REPO_ROOT / "scripts"
    if not (scripts_dir / "sync.sh").is_file():
        errors.append("scripts/sync.sh ausente")
    return errors


def main():
    all_errors = []
    all_errors += check_root_files()
    all_errors += check_projects()
    all_errors += check_knowledge()
    all_errors += check_templates()
    all_errors += check_skills()
    all_errors += check_logs()
    all_errors += check_scripts()

    if all_errors:
        print("❌ Estrutura do BrunoOS com problemas:\n")
        for e in all_errors:
            print(f"  - {e}")
        sys.exit(1)

    print("✅ Estrutura do BrunoOS válida.")
    sys.exit(0)


if __name__ == "__main__":
    main()

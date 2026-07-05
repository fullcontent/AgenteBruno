#!/bin/bash
set -euo pipefail

# Diretório do BrunoOS na VPS (espelha a estrutura deste repositório)
HERMES_DIR="$HOME/.hermes"

# Diretório raiz do repositório (pai de scripts/)
REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"

ROOT_FILES=(README.md SOUL.md USER.md GOALS.md DECISION_RULES.md THINKING.md WORKFLOW.md WRITING_STYLE.md PROJECTS.md NOW.md IDEAS.md HERMES.md)
FOLDERS=(projects knowledge templates skills archive logs memories scripts)

echo "⏳ Iniciando sincronização do BrunoOS..."

mkdir -p "$HERMES_DIR"

echo "📦 Sincronizando root files..."
for f in "${ROOT_FILES[@]}"; do
    if [ -f "$REPO_DIR/$f" ]; then
        cp -v "$REPO_DIR/$f" "$HERMES_DIR/"
    else
        echo "⚠️ Root file ausente: $f"
    fi
done

echo "📁 Sincronizando pastas..."
for d in "${FOLDERS[@]}"; do
    if [ -d "$REPO_DIR/$d" ]; then
        mkdir -p "$HERMES_DIR/$d"
        cp -rv "$REPO_DIR/$d"/. "$HERMES_DIR/$d/" 2>/dev/null || true
    else
        echo "⚠️ Pasta local ausente: $d"
    fi
done

echo "✅ Sincronização concluída com sucesso!"
echo "Os arquivos do BrunoOS estão prontos em $HERMES_DIR"

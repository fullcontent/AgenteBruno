#!/bin/bash
set -euo pipefail

# Configurações de diretórios
HERMES_DIR="$HOME/.hermes"
HERMES_CONTEXT_DIR="$HERMES_DIR/context"
HERMES_SKILLS_DIR="$HERMES_DIR/skills"
HERMES_MEMORY_DIR="$HERMES_DIR/memory"

# Diretório raiz do repositório (pai de scripts/)
REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"

ROOT_FILES=(AGENTS.md SOUL.md USER.md GOALS.md MAPA.md MEMORY.md TOOLS.md PROPAGATION.md HERMES.md agent-os.yaml)

echo "⏳ Iniciando sincronização do Agente Bruno..."

# 1. Garantir que os diretórios globais do Hermes existem
mkdir -p "$HERMES_CONTEXT_DIR" "$HERMES_SKILLS_DIR" "$HERMES_MEMORY_DIR"

# 2. Copiar os root files
echo "📦 Sincronizando root files..."
for f in "${ROOT_FILES[@]}"; do
    if [ -f "$REPO_DIR/$f" ]; then
        cp -v "$REPO_DIR/$f" "$HERMES_CONTEXT_DIR/"
    else
        echo "⚠️ Root file ausente: $f"
    fi
done

# 3. Sincronizando as skills (recursivo, preserva skills/{categoria}/{nome}/SKILL.md)
if [ -d "$REPO_DIR/skills" ]; then
    echo "🛠️ Sincronizando skills..."
    cp -rv "$REPO_DIR/skills"/* "$HERMES_SKILLS_DIR/"
else
    echo "⚠️ Diretório local de skills não encontrado!"
fi

# 4. Sincronizando memory
if [ -d "$REPO_DIR/memory" ]; then
    echo "🧠 Sincronizando memory..."
    cp -v "$REPO_DIR/memory"/*.md "$HERMES_MEMORY_DIR/"
else
    echo "⚠️ Diretório local de memory não encontrado!"
fi

echo "✅ Sincronização concluída com sucesso!"
echo "Os arquivos do seu agente estão prontos em $HERMES_DIR"

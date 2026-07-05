#!/bin/bash
set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
HERMES_HOME="${HERMES_HOME:-$HOME}"

cd "$REPO_DIR"

git pull --ff-only
HOME="$HERMES_HOME" ./scripts/sync.sh
python3 ./scripts/validate-brunos.py

#!/usr/bin/env bash
# Test e2e local : installe l'environnement si besoin, regenere le one-pager
# et execute la suite pytest complete. Sortie 0 = tout est vert.
set -euo pipefail
cd "$(dirname "$0")"

PYTHON_BIN="${PYTHON_BIN:-python3}"
if command -v python3.13 >/dev/null 2>&1; then
  PYTHON_BIN=python3.13
fi

if [ ! -x .venv/bin/python ]; then
  echo "== Creation du venv (${PYTHON_BIN}) =="
  "$PYTHON_BIN" -m venv .venv
fi

echo "== Installation des dependances epinglees =="
.venv/bin/pip install --quiet -r requirements.txt

echo "== Generation du one-pager docs/index.html =="
.venv/bin/python scripts/generate_onepager.py

echo "== Suite de tests pytest =="
.venv/bin/pytest -v

echo "== E2E OK =="

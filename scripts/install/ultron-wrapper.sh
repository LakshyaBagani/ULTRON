#!/usr/bin/env bash
# ultron-wrapper.sh — symlinked to ~/.local/bin/ultron.
# Activates the managed venv and execs the real ultron CLI.

ULTRON_HOME="${ULTRON_HOME:-$HOME/.ultron}"
VENV="$ULTRON_HOME/.venv"

if [[ ! -d "$VENV" ]]; then
    echo "ultron: venv not found at $VENV" >&2
    echo "Re-run the installer: curl -fsSL https://ultron.github.io/Ultron/install.sh | bash" >&2
    exit 1
fi

exec "$VENV/bin/ultron" "$@"

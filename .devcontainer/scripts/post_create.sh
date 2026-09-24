#!/usr/bin/env bash
set -euo pipefail

USER_NAME="${USER:-vscode}"

echo "Configuring zsh history..."
sudo mkdir -p /commandhistory
sudo touch /commandhistory/.zsh_history
sudo chown -R "${USER_NAME}" /commandhistory
if ! grep -q "HISTFILE=/commandhistory/.zsh_history" "${HOME}/.zshrc" 2>/dev/null; then
  {
    echo 'autoload -Uz add-zsh-hook'
    echo 'append_history() { fc -W }'
    echo 'add-zsh-hook precmd append_history'
    echo 'export HISTFILE=/commandhistory/.zsh_history'
  } >> "${HOME}/.zshrc"
fi

# poe → uv run poe
if ! grep -q "alias poe=" "${HOME}/.zshrc" 2>/dev/null; then
  echo "alias poe='uv run poe'" >> "${HOME}/.zshrc"
fi

echo "uv sync ..."
uv sync

echo "done"

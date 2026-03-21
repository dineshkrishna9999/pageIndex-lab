#!/usr/bin/env bash
set -euo pipefail

USERNAME=vscode

echo "==> Configuring zsh theme ..."
sed -i 's/^ZSH_THEME=".\+"$/ZSH_THEME="ys"/g' ~/.zshrc

echo "==> Configuring zsh history ..."
sudo mkdir -p /commandhistory
sudo touch /commandhistory/.zsh_history
sudo chown -R "$USERNAME" /commandhistory

SNIPPET='export PROMPT_COMMAND="history -a" && export HISTFILE=/commandhistory/.zsh_history'
echo "$SNIPPET" >> "/home/$USERNAME/.zshrc"

echo "==> Installing Python dependencies ..."
uv sync

echo "==> Post-create setup complete!"

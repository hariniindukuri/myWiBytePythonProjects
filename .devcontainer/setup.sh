#!/bin/bash
set -e

echo "🛠️ Configuring WiByte Python Lab environment..."
TARGET_RC="/etc/bash.bashrc"

# 1. Set display server for X11 / Tkinter / Turtle
if ! grep -q "DISPLAY=:1" "$TARGET_RC"; then
    echo "export DISPLAY=:1" >> "$TARGET_RC"
fi

# Target the explicit vscode user bashrc as well as global bashrc
for RC_FILE in "/home/vscode/.bashrc" "/etc/bash.bashrc"; do
    if [ -f "$RC_FILE" ] && ! grep -q "WiByte Python Lab" "$RC_FILE"; then
        echo 'export PS1="\[\033[01;32m\]WiByte Python Lab 1.1\[\033[00m\] >> "' >> "$RC_FILE"
    fi
done

# 3. Secret Instructor Recovery Alias (vnc-rerun)
if ! grep -q "vnc-rerun" "$TARGET_RC"; then
    RECOVERY_CMD="alias vnc-rerun='sudo pkill -9 -f Xvfb; sudo pkill -9 -f fluxbox; sudo pkill -9 -f websockify; sudo pkill -9 -f x11vnc; sudo rm -rf /tmp/.X1-lock /tmp/.X11-unix; sleep 1; sudo nohup /usr/local/share/desktop-init.sh > /tmp/desktop-lite.log 2>&1 & sleep 3; echo \"✅ VNC desktop restarted successfully!\"'"
    echo "$RECOVERY_CMD" >> "$TARGET_RC"
fi

echo "✅ Environment Setup complete, Ports/UI customization starts now."



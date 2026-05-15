#!/bin/sh
# mtype uninstaller — POSIX sh.
# Run as user for ~/.local/bin, or with sudo for /usr/local/bin.

set -eu

if [ "$(id -u)" -eq 0 ]; then
    TARGET_DIR="/usr/local/bin"
    SCOPE="system-wide"
else
    TARGET_DIR="${HOME}/.local/bin"
    SCOPE="user-local"
fi

TARGET="$TARGET_DIR/mtype"

# -e fails for dangling symlinks, so check -L too (covers the legacy
# symlink-based install).
if [ -e "$TARGET" ] || [ -L "$TARGET" ]; then
    rm -f "$TARGET"
    echo "removed mtype ($SCOPE) from $TARGET"
else
    echo "mtype not found at $TARGET; nothing to remove"
fi

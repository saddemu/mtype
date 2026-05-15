#!/bin/sh
# mtype installer — POSIX sh, works on any Linux.
# Run as user for ~/.local/bin install, or with sudo for /usr/local/bin.

set -eu

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SOURCE="$SCRIPT_DIR/mtype.py"

if [ ! -f "$SOURCE" ]; then
    echo "error: mtype.py not found next to install.sh ($SCRIPT_DIR)" >&2
    exit 1
fi

if [ "$(id -u)" -eq 0 ]; then
    TARGET_DIR="/usr/local/bin"
    SCOPE="system-wide"
else
    TARGET_DIR="${HOME}/.local/bin"
    SCOPE="user-local"
fi

TARGET="$TARGET_DIR/mtype"

mkdir -p "$TARGET_DIR"
rm -f "$TARGET"
cp "$SOURCE" "$TARGET"
chmod 755 "$TARGET"

echo "installed mtype ($SCOPE) -> $TARGET"

if ! command -v python3 >/dev/null 2>&1; then
    echo "warning: python3 not found in PATH; mtype needs Python 3.8+" >&2
fi

if [ "$SCOPE" = "user-local" ]; then
    case ":${PATH}:" in
        *":${TARGET_DIR}:"*) ;;
        *)
            {
                echo
                echo "warning: $TARGET_DIR is not in your PATH."
                echo "add this line to your shell rc (~/.bashrc, ~/.zshrc, …):"
                echo "  export PATH=\"\$HOME/.local/bin:\$PATH\""
            } >&2
            ;;
    esac
fi

echo "run 'mtype --help' to get started."

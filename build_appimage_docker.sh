#!/bin/bash

# Docker-based AppImage builder for OneDriveGUI
# Allows building AppImages on non-Debian systems (e.g. Arch Linux)
# using an Ubuntu Noble container with appimage-builder.

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "=== OneDriveGUI Docker AppImage Builder ==="
echo ""

# Check Docker is available
if ! command -v docker &> /dev/null; then
    echo "Error: docker not found. Please install Docker first."
    exit 1
fi

# Build the AppImage inside an Ubuntu Noble container
docker run \
    --cap-add SYS_ADMIN \
    --device /dev/fuse \
    --security-opt apparmor:unconfined \
    --rm \
    -v "$SCRIPT_DIR:/OneDriveGUI" \
    ubuntu:noble \
    bash -c '
set -e
echo "Installing dependencies..."
apt update
apt install -y wget python3 python3-pip fuse gtk-update-icon-cache

echo "Installing appimage-builder..."
wget -q -O /tmp/appimage-builder.AppImage https://github.com/AppImageCrafters/appimage-builder/releases/download/v1.1.0/appimage-builder-1.1.0-x86_64.AppImage
chmod +x /tmp/appimage-builder.AppImage
mv /tmp/appimage-builder.AppImage /usr/local/bin/appimage-builder

echo ""
echo "Building AppImage..."
cd /OneDriveGUI/
./build_appimage.sh

echo ""
echo "Fixing ownership of build artifacts..."
chown -R '"$(id -u)"':'"$(id -g)"' /OneDriveGUI/AppDir 2>/dev/null || true
# Fix ownership of the generated AppImage
chown '"$(id -u)"':'"$(id -g)"' /OneDriveGUI/OneDriveGUI-*.AppImage 2>/dev/null || true
'

echo ""
echo "=== Build complete ==="
ls -lh "$SCRIPT_DIR"/OneDriveGUI-*.AppImage 2>/dev/null || echo "No AppImage found in $SCRIPT_DIR"

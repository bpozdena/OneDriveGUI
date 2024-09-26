#!/bin/bash

# Step 1: Extract version from src/version.py
VERSION=$(python3 -c "from src.version import __version__; print(__version__)")
if [ -z "$VERSION" ]; then
  echo "Failed to extract version from src/version.py"
  exit 1
fi
echo "Extracted version: $VERSION"

# Step 2: Update the indented version line in AppImageBuilder.yml
YAML_FILE="AppImageBuilder.yml"
if [ -f "$YAML_FILE" ]; then
  echo "Updating version in $YAML_FILE..."
  # Use sed to match the indented version line (e.g., "    version: 1.1.0") and update it
  sed -i "s/^\(\s\+version:\s\).*/\1$VERSION/" "$YAML_FILE"
  echo "Version updated to $VERSION in the indented version line of $YAML_FILE"
else
  echo "$YAML_FILE not found."
  exit 1
fi

# Step 3: Build the AppImage using appimage-builder
if ! command -v appimage-builder &> /dev/null; then
  echo "appimage-builder could not be found. Please install it first."
  exit 1
fi

echo "Building AppImage..."
appimage-builder --recipe "$YAML_FILE"

if [ $? -eq 0 ]; then
  echo "AppImage build succeeded!"
else
  echo "AppImage build failed."
  exit 1
fi

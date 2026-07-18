#!/bin/bash

# Step 1: Function to extract version from OneDriveGUI.py without importing
get_version() {
  FILE_PATH="src/onedrive_gui/options.py"
  VERSION=$(grep -Po '^version\s*=\s*"\K[^\"]+' "$FILE_PATH")
  
  if [ -z "$VERSION" ]; then
    echo "Failed to extract version from $FILE_PATH"
    exit 1
  fi
  
  echo "Extracted version: $VERSION"
}

# Step 2: Update the indented version line in AppImageBuilder.yml
update_yaml() {
  YAML_FILE="AppImageBuilder.yml"
  
  if [ -f "$YAML_FILE" ]; then
    echo "Updating version in $YAML_FILE..."
    # Use sed to match the indented version line and update it
    sed -i "s/^\(\s\+version:\s\).*/\1$VERSION/" "$YAML_FILE"
    echo "Version updated to $VERSION in the indented version line of $YAML_FILE"
  else
    echo "$YAML_FILE not found."
    exit 1
  fi
}

# Step 3: Update the indented version line in pyproject.toml
update_pyproject() {
  PYPROJECT_TOML_FILE="pyproject.toml"
  
  if [ -f "$PYPROJECT_TOML_FILE" ]; then
    echo "Updating version in $PYPROJECT_TOML_FILE..."
    # Use sed to match the indented version line and update it
    sed -i "s/^\(version =\).*/\1 \"$VERSION\"/" "$PYPROJECT_TOML_FILE"
    echo "Version updated to $VERSION in the indented version line of $PYPROJECT_TOML_FILE"
  else
    echo "$PYPROJECT_TOML_FILE not found."
    exit 1
  fi
}

# Step 4: Build the AppImage using appimage-builder
build_appimage() {
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
}

# Main script execution
get_version
update_yaml
update_pyproject
build_appimage

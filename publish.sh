#!/bin/bash

# Exit on error
set -e

# Load environment variables from .env
if [ -f .env ]; then
    export $(cat .env | xargs)
fi

echo "🚀 Starting publish process..."

# Run tests
echo "🧪 Running tests..."
pytest tests/ -v

# Extract current version and bump minor version
echo "📦 Bumping minor version..."
current_version=$(grep -Po '(?<=version = ")[^"]*' pyproject.toml)
IFS='.' read -r major minor patch <<< "$current_version"
new_minor=$((minor + 1))
new_version="$major.$new_minor.0"

# Update version in pyproject.toml
echo "📝 Updating version to $new_version..."
sed -i "s/version = \"$current_version\"/version = \"$new_version\"/" pyproject.toml

# Clear dist directory
echo "🧹 Clearing dist directory..."
rm -rf dist/*

# Build using uv
echo "🔨 Building package..."
uv build

# Publish using uv
echo "📤 Publishing to PyPI..."
uv publish

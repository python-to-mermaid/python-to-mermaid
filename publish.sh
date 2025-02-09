#!/bin/bash

# Exit on error
set -e

echo "🚀 Starting publish process..."

# Minor version bump using uv
echo "📦 Bumping minor version..."
uv lock --upgrade-package python-to-mermaid

# Clear dist directory
echo "🧹 Clearing dist directory..."
rm -rf dist/*

# Build using uv
echo "🔨 Building package..."
uv build

# Publish using uv
echo "📤 Publishing to PyPI..."
uv publish



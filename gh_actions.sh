#!/bin/sh
if [ "$GITHUB_ACTIONS" != "true" ]; then
  echo "Not running in GitHub Actions environment. Exiting..."
  exit 1
fi

EXERCISE_DIR="gne_exercises"
CURRENT_DIR=$(pwd)
REPO="twin-bridges/gne_exercises"
cd ..

if [ ! -d "$EXERCISE_DIR" ]; then
  mkdir "$EXERCISE_DIR"
fi

if [ -d "$EXERCISE_DIR" ]; then
  cd "$EXERCISE_DIR"
  git init --initial-branch=main
  git remote add origin https://github.com/"$REPO"
  git pull origin main
  # Ensure we get the tags
  git fetch origin
fi

cd "$CURRENT_DIR"

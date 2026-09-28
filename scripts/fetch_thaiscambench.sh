#!/usr/bin/env bash
set -euo pipefail

mkdir -p external

if [ -d "external/ThaiScamBench/.git" ]; then
  echo "ThaiScamBench already exists. Updating..."
  git -C external/ThaiScamBench pull --ff-only
else
  git clone https://github.com/nutthakorn7/ThaiScamBench.git external/ThaiScamBench
fi

echo "ThaiScamBench is available at external/ThaiScamBench"

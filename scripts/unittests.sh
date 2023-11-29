#!/usr/bin/env bash

REPO_DIR="$(git rev-parse --show-toplevel)"

(cd "$REPO_DIR" && python -m pytest --doctest-modules --junitxml=junit/test-results.xml)

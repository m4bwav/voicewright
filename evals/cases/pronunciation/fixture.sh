#!/usr/bin/env bash
# Runs only with `claude plugin eval --scaffold`.
set -euo pipefail
cat > lines.json <<'JSON'
[
 {
  "id": "l1",
  "text": "A cry from the bow of the ship."
 }
]
JSON

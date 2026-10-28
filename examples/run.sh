#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
PYTHONPATH=src python -m gbt_pipeline_versions info
PYTHONPATH=src python -m gbt_pipeline_versions check --payload '{"name": "<在此填写>"}'
PYTHONPATH=src python -m gbt_pipeline_versions run   --payload '{"name": "<在此填写>"}'

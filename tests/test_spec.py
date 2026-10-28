"""The spec must match the registry exactly. Drift fails here, not in production."""

from __future__ import annotations

import json
import re
from pathlib import Path

from gbt_pipeline_versions import SPEC
from gbt_pipeline_versions.spec import _RAW

REGISTRY = json.loads(_RAW)


def test_identity():
    assert SPEC.name == "pipeline_versions"
    assert SPEC.domain == "pipeline"
    assert SPEC.handler == REGISTRY["handler"]


def test_description_is_verbatim():
    assert SPEC.desc == REGISTRY["desc"]
    assert SPEC.desc.strip(), "an empty description would make the page useless"


def test_flags_are_consistent():
    assert SPEC.gated is (not SPEC.safe)
    assert SPEC.as_dict()["ops"] == list(SPEC.ops)
    assert SPEC.as_dict()["params"] == list(SPEC.params)


def test_serialisation_round_trips():
    data = SPEC.as_dict()
    assert data["gated"] == SPEC.gated
    assert json.loads(json.dumps(data, ensure_ascii=False))["name"] == "pipeline_versions"


def test_summary_is_not_empty():
    assert SPEC.summary.strip()
    assert len(SPEC.summary) <= len(SPEC.desc)

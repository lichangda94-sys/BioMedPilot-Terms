from __future__ import annotations

import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "query_fragment.schema.json"
EXAMPLES_DIR = ROOT / "examples" / "query_fragments"
ALLOWED_STATUS = {"example", "candidate", "review_required"}
FORBIDDEN_KEYS = {
    "api" + "_key",
    "pass" + "word",
    "to" + "ken",
    "se" + "cret",
}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def collect_keys(value) -> set[str]:
    keys: set[str] = set()
    if isinstance(value, dict):
        for key, nested in value.items():
            keys.add(str(key).lower())
            keys.update(collect_keys(nested))
    elif isinstance(value, list):
        for item in value:
            keys.update(collect_keys(item))
    return keys


SCHEMA = load_json(SCHEMA_PATH)
VALIDATOR = Draft202012Validator(SCHEMA)
EXAMPLE_FILES = sorted(EXAMPLES_DIR.glob("*.json"))


@pytest.mark.parametrize("path", EXAMPLE_FILES, ids=lambda path: path.name)
def test_query_fragment_examples_validate_against_schema(path: Path) -> None:
    data = load_json(path)
    VALIDATOR.validate(data)


@pytest.mark.parametrize("path", EXAMPLE_FILES, ids=lambda path: path.name)
def test_query_fragment_example_status_is_public_safe(path: Path) -> None:
    data = load_json(path)
    assert data["status"] in ALLOWED_STATUS
    assert data["status"] not in {"reviewed", "production"}


@pytest.mark.parametrize("path", EXAMPLE_FILES, ids=lambda path: path.name)
def test_query_fragment_examples_do_not_use_forbidden_keys(path: Path) -> None:
    data = load_json(path)
    keys = collect_keys(data)
    assert keys.isdisjoint(FORBIDDEN_KEYS)

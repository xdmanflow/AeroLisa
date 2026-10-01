"""Smoke tests: the package and every component import cleanly."""

import importlib

import pytest

import aerolisa

COMPONENTS = [
    "aerolisa.core",
    "aerolisa.cli",
    "aerolisa.pipelines",
    "aerolisa.modules.market",
    "aerolisa.modules.engine_health",
    "aerolisa.modules.fleet",
    "aerolisa.modules.operations",
    "aerolisa.modules.trajectory",
    "aerolisa.planner",
    "aerolisa.api",
    "aerolisa.copilot",
]


def test_version():
    assert aerolisa.__version__ == "0.0.1"


@pytest.mark.parametrize("name", COMPONENTS)
def test_component_imports(name):
    assert importlib.import_module(name) is not None

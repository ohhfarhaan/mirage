"""Foundation smoke test: the top-level packages import cleanly."""

import importlib

import pytest


@pytest.mark.parametrize("package", ["honeypot", "analyzer", "api", "llm"])
def test_package_imports(package: str) -> None:
    module = importlib.import_module(package)
    assert module.__doc__

# tests/unit/conftest.py
import pytest

from my_project.core.maths_operations import add

def test_add(sample_data: tuple[int, int]):
    # a, b = sample_data
    assert add(**sample_data) == 3
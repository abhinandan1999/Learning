# !pytest tests/unit/core/test_math_operations.py

# tests/unit/conftest.py
import pytest

from my_project.core.maths_operations import add

@pytest.mark.smoke
def test_add2(sample_data: tuple[int, int]):
    # a, b = sample_data
    assert add(**sample_data) == 3

@pytest.mark.smoke
@pytest.mark.parametrize("sample_data, expected_result", [
    ({"x": 1, "y": 2}, 3),
    ({"x": 2, "y": 3}, 5),
    ({"x": 3, "y": 4}, 7),
])
def test_add(sample_data: dict[str, int], expected_result: int):
    assert add(**sample_data) == expected_result

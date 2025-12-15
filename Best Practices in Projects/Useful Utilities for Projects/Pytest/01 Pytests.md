### Fixtures: Managing state and Dependencies

pytest Fixtures are way of Providing data, test doubles, or state setup to your tests.
Fixtures are functions that can return wide range of values. Each test that depends on a fixture must 
explicitly accept that fixture as an argument.

### Example of Fixtures
```python
@pytest.fixture
def sample_data():
    return [1, 2, 3, 4, 5]
```
- `sample_data` is a fixture function that returns a list of numbers.
- Think of it like a data provider for your tests.

Note: It is good practice to name fixtures descriptively and it is maintained in a separate file called `conftest.py`
- `sample_data` should be argument to the test function

### Markers: Customizing Test Execution
Pytest enables us to define categories of tests and run them selectively.

```python
@pytest.mark.smoke
def test_add(sample_data: tuple[int, int]):
    # a, b = sample_data
    assert add(**sample_data) == 3
```
```bash
pytest -m smoke
```


Tip: Because any marker name can be used, it is advised to use --strict-markers option to pytest to ensure that only markers defined in pytest.ini are used.


### Parametrization: Running Tests with Different Data
Parametrization allows you to run the same test with different inputs.
```python
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (2, 3, 5),
    (3, 4, 7),
])
def test_add(a, b, expected):
    assert add(a, b) == expected
```




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


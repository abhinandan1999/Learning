#### Prepare your project
- Include `[build-system]` section in `pyproject.toml`

#### Build your project
- Run `uv build`

#### Get the version of your project
- Run `uv version`

#### Publish your project
- Run `uv publish`

#### Publish your project to TestPyPI
- Run `uv publish --index testpypi`

Note: Make sure to add [[tool.uv.index]] section in `pyproject.toml` with the index URL
```
[[tool.uv.index]]
name = "testpypi"
url = "https://test.pypi.org/simple/"
publish-url = "https://test.pypi.org/legacy/"
explicit = true
```


# PTest - python based testing solution

**Run tests**
```
pytest
pytest -v
```

**Markers**
```
pytest --markers
pytest -m login
pytest -m smoke -v

Logical "AND" - pytest -m "account and login"
Logical "OR" - pytest -m "account or login"
```

**Report**
```
pytest --html="report.html"
pytest --junitxml="result.xml"
```

**Pytest argparse** ``pytest -m=environment --env=dev -v``

**Handling skips** ``pytest -m=environment --env=dev -v -rs``

**Expected failures** ``pytest -m=environment --env=dev -v -rx``

**Browsers**
```
Single browser approach - pytest -m=login
Parallel browser approach - pytest -m=e2e
```

**Sample test data parameterization** ``pytest -m=tv -s -v``

**Test data parameterization from external file** ``pytest -m=external_data -s -v``

**Parallel execution**
```
pip install pytest-xdist
pytest -m=parallel -s -v -n4 (n4 - count of nodes)
pytest -m=parallel -s -v -nauto
```



# PTest - sample pytest ATF structure

## Note on Codespaces Virtualenv 
Checkout how if you run `pip freeze | wc -l` there are many packages we may not want
Try `which python`
1. `virtualenv ~/.venv` 
2. Always source this virt env:
`vim ~/.bashrc` and put in `source ~/.venv/bin/activate`
3. Verify the right python `which python` and try `pip freeze | wc -l` it should be 0

## Make file
* `make install` install the project dependencies
* `make test` perform tests execution and coverage stat
* `make format` formatting the code
* `make lint` static code validation
* `make all` perform all operations (from step 1 to step 4) one after each other

## Run tests
* `python -m pytest -vv -m deposit` run tests by a single marker
* `python -m pytest -vv -m "deposit or withdraw"` run tests by multiple markers
* `python -m pytest -vv -m "not deposit"` exclude some marks from execution

* `-s` to see the prints

## List of markers
`pytest --markers` get back the list of markers (custom and default)

## Add option to run the tests with different configs
* `config.py` - set up the configuration
* `conftest` - add option and fixture for usage
* `test_account_config_usage.py` - example of usage custom option
* `pytest -h` - custom option should be added to the Custom options section for pytest help
* `python -m pytest --env dev -vv -m test_dev_config` - usage of custom option


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



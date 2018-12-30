# PTest - python based testing solution

*run tests*

```
pytest
pytest -v
```

*markers*

```
pytest --markers
pytest -m login
pytest -m smoke -v
```

*logical AND*

```
pytest -m "account and login"
```

*logical OR*

```
pytest -m "account or login"
```

*report*

```
pytest --html="report.html"
pytest --junitxml="result.xml"
```

*pytest argparse*

```
pytest -m=environment --env=dev -v
```

*handling skips*

```
pytest -m=environment --env=dev -v -rs
```

*expected failures*

```
pytest -m=environment --env=dev -v -rx
```
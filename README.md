# Malicious PyPI Template

Malicious PyPI package template with python reverse shell.

- How to use: change inserted code, create package, upload package
- Procedure:

```bash
python setup.py sdist bdist_wheel
twine upload --repository imqwe dist/* # use this command if .pypirc is configed.
twine upload --repository-url http://localhost:port/ -u your-username -p your-password dist/* # use this command if .pypirc is not configed
```

# Malicious PyPI Template

Malicious PyPI package template with python reverse shell.

- Dependent tools: pip, twine
- Usage: change inserted code, create package, upload package
- Procedure:

```bash
python setup.py sdist bdist_wheel
twine upload --repository imqwe dist/* # use this command if .pypirc is configed.
twine upload --repository-url http://localhost:port/ -u your-username -p your-password dist/* # use this command if .pypirc is not configed
```

- package directory structure

```
├── dist
│   └── imqwe-0.0.1.tar.gz
├── README.md
├── rshell
│   └── __init__.py
├── setup.cfg
└── setup.py
```

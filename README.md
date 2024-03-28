# Custom hooks

A repository with custom git pre-commit hooks.

## Commit message hook

Add to `.pre-commig-config.yaml`:

```
repos:
  - repo: https://github.com/pytholic/git-custom-precommit-hooks.git
    rev: main
    hooks:
      - id: check-commit-msg
```

Then run:

```
pre-commit install --hook-type commit-msg
```

To run the tests:

```
cd tests
python test_commit_msg_hook.py
```

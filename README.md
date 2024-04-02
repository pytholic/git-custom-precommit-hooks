# Custom hooks

A repository with custom git pre-commit hooks.

## Commit message hook

Add to `.pre-commit-config.yaml`:

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

To test, create a branch MOPS-XXX and run:

```
cd tests
python test_commit_msg_hook.py
```

You can modify the following regex inside `commit_msg_hook.sh` according to your needs.

```
msg_regex='^\[(feat|fix|docs|style|refactor|test|chore)\]\[MOPS-[0-9]+\] .+$'
```

### Note

It does not work with the `main/master` branches. Your branch should be of the format defined in regex like MOPS-123. You can push the initial main branch without it and add the hook to child branches.

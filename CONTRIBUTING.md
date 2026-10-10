# Contributing to schedule-ng

Thanks for helping keep schedule alive. Bug reports, fixes and documentation
improvements are all welcome.

## What schedule-ng is (and isn't)

schedule-ng is a small, dependency-free, in-process scheduler with a
human-friendly API, and a drop-in replacement for
[schedule](https://github.com/dbader/schedule). That shapes what gets merged:

- **Backward compatibility comes first.** Code written for schedule 1.2 should
  keep working. Behaviour changes need a strong reason and a changelog entry.
- **No required dependencies.**
- **Supported Python versions** are those that haven't reached their end of life.
  A version is dropped in the first minor release after its end-of-life date.
- **Small scope.** Features such as job persistence, retries, distributed
  execution or a full cron syntax are out of scope. If you need those,
  [APScheduler](https://github.com/agronholm/apscheduler) is a great choice.
  If you're unsure whether a feature fits, open an issue before writing code.

## Reporting a bug

Please include:

- your schedule-ng and Python versions, and your operating system;
- a minimal code example that shows the problem;
- what you expected to happen, and what happened instead.

For timing problems, mention your local timezone and whether a daylight saving
time change was involved.

## Pull requests

1. Set up a development environment as described in the
   [development guide](https://schedule-ng.readthedocs.io/en/latest/development.html).
2. **Bug fixes need a test that fails without the fix.** Features need tests too.
   Coverage must stay at 100% of lines and branches; CI fails otherwise. Test
   behaviour a user could notice, and delete code that can't be reached instead
   of excluding it with `# pragma: no cover`.
3. Keep pull requests focused on one change.
4. Add an entry to `HISTORY.rst` for anything users will notice.
5. Make sure `uv run pytest`, `uv run ruff check`, `uv run ruff format --check`
   and `uv run mypy` pass. CI runs them on Linux, macOS and Windows.

## AI-assisted contributions

Using AI tools is fine; this project uses them too. What matters is that you
understand and stand behind every line you submit: you've read it, tested it,
and can explain it in review. Pull requests that look generated and
unreviewed, such as large unrelated changes or untested code, may be closed.

## License

By contributing, you agree that your contributions will be licensed under the
[MIT License](LICENSE.txt).

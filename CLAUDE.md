# schedule-ng

A maintained, drop-in compatible fork of [dbader/schedule](https://github.com/dbader/schedule):
an in-process job scheduler in a single module, `schedule_ng/__init__.py`, with tests in
`test_schedule.py`. Users switch with `import schedule_ng as schedule`, so the public API is a contract.

## Ground rules

- **The maintainer reviews and merges everything.** Work on a branch and open a pull request. Never push
  to `main`, never push tags, never approve releases, and never post comments, reviews or replies on
  GitHub (in this repo or upstream) unless explicitly asked to in that session. Draft replies instead.
- **Bug fixes start with a failing test.** Write the test, show it fails on the current code, then fix.
  Say in the PR description that you checked this.
- **Keep the API backward compatible** with schedule 1.2. That includes exception types, the
  `"schedule"` logger name, `Job.next_run` and `Job.last_run` being naive local datetimes, and
  `repr()`/`str()` output where possible. Any behaviour change needs a strong reason, a test, and an
  entry in `HISTORY.rst` marked as a behaviour change.
- **Security.** Pin GitHub Actions to full commit SHAs (with a `# vX.Y.Z` comment), keep workflow
  permissions minimal, and keep `zizmor` and ruff's `S` rules passing. Runner images are pinned
  (`ubuntu-26.04`, `macos-26`, `windows-2025`); bump them in their own PR when GitHub announces a
  retirement. Never weaken these to get CI
  green. Security reports go through private advisories (`SECURITY.md`), never public issues.
- **No new runtime dependencies.** pytz stays optional; the code must work with `zoneinfo` alone.
- **Small, focused commits and PRs.** No drive-by refactors or bulk reformatting mixed with fixes.
- **Stay in scope.** Decline persistence, retries, distributed execution, job stores and full cron
  syntax; point users to APScheduler. Ask the maintainer before starting any feature.
- **Credit contributors.** When reusing an upstream or community PR, apply it with `git am` so the
  author keeps authorship, or add a `Co-authored-by:` trailer when adapting it.
- If you can't explain why a change is correct, don't propose it. Prefer saying "I'm not sure" in the
  PR over guessing.

## Commands

```bash
uv run pytest                    # tests (also run without pytz: they skip cleanly)
uv run ruff check                # lint
uv run ruff format --check       # formatting
uv run mypy                      # types
uv run --only-group docs --with-editable . sphinx-build -W -b html docs docs/_build/html
```

CI must stay green on Linux, macOS and Windows for Python 3.11 to 3.15, including the free-threaded builds.
Code must run on the oldest supported Python (`requires-python` in `pyproject.toml`). Python versions
are dropped in the first minor release after their end of life, never in a patch release. Don't
rewrite working code just to use newer syntax; use it in code that is changing anyway.

## How scheduling works

- Jobs store their next run as an aware UTC datetime in `Job._next_run`. The public `next_run`
  property converts it to a naive local datetime; its setter accepts naive (local) or aware values.
- `should_run`, sorting and `idle_seconds` compare in UTC, because local times repeat when clocks
  go back.
- Seconds, minutes and hours measure **elapsed time**. Days and weeks follow the **wall clock** of
  the job's timezone (`at_time_zone`, or local time if unset).
- `_localize(wall, tz)` converts wall-clock times to UTC: a repeated time resolves to its first
  occurrence; a time in a DST gap moves forward by the size of the gap (02:30 becomes 03:30).
  It handles pytz (`localize`), other `tzinfo` objects and local time (`tz=None`).

## Testing time-dependent code

- `mock_datetime(...)` freezes the clock. It simulates the local timezone with `zoneinfo` (via
  `posix_zone()`), because `time.tzset()` doesn't exist on Windows. The default local zone is Berlin.
- `poll_across(scheduler, zone, start_utc, end_utc)` polls a scheduler minute by minute across a
  real UTC timeline. Use it for anything involving DST changes.
- After writing a test, check it fails without the fix, for example with
  `git stash -- schedule_ng/__init__.py`.

## Triage and review

- **New issues:** try to reproduce bugs with a failing test before anything else, and report
  whether it reproduced. Draft a reply for the maintainer; don't post it.
- **External PRs:** check out the branch, run the full checks, read every line, and summarise for the
  maintainer: what it fixes, whether it has a failing-first test, compatibility risks, and a
  recommendation. Don't merge.

## Releases (maintainer only)

Bump `__version__` in `schedule_ng/__init__.py` and `release` in `docs/conf.py`, update
`HISTORY.rst` and `AUTHORS.rst`, merge, then the maintainer pushes a `vX.Y.Z` tag and approves the
`pypi` deployment. PyPI versions can never be re-uploaded, so double-check before tagging.

## Environment notes

- The maintainer works on Windows. `gh` is at `C:\Program Files\GitHub CLI\gh.exe` and may not be on
  `PATH` in Git Bash.

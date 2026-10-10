.. :changelog:

History
-------

1.5.0 (2026-10-10)
++++++++++++++++++

Issue numbers refer to the original
`dbader/schedule <https://github.com/dbader/schedule>`_ repository.

- Add ``.weekday`` and ``.weekend`` (#99, #129, #232, #297, #511, #556, #607).
  ``every().weekday.at("09:00")`` runs once a day from Monday to Friday;
  ``every(5).minutes.weekday`` keeps its interval but skips Saturdays and
  Sundays, and starts again at midnight on Monday.
- Add ``.between(start, end, tz=None)`` for jobs that run every few seconds,
  minutes or hours (#182, #231, #260, #347, #481, #568, #597).
  ``every(5).minutes.between("09:00", "17:00")`` runs only from 09:00 to
  17:00, both included. The window can cross midnight, have its own timezone,
  and be combined with ``.weekday`` and ``.weekend``.
- GitHub releases now include the sdist and wheel, signed with
  `Sigstore <https://www.sigstore.dev/>`_. The release notes show how to
  verify them.

1.4.0 (2026-10-10)
++++++++++++++++++

Issue numbers refer to the original
`dbader/schedule <https://github.com/dbader/schedule>`_ repository.

- **Require Python 3.11 or newer.** Python 3.9 and 3.10 have reached their end
  of life; pip keeps installing schedule-ng 1.3.1 on them.
- Support Python 3.15, including the free-threaded build.
- Fix and complete the type hints (#559). Intervals and ``to()`` accept
  floats, ``at()`` accepts any ``tzinfo``, and the builder methods return
  ``Self``, so chains on ``Job`` subclasses keep their type. The package now
  passes ``mypy --strict``.
- Document the Python support policy: every Python version that has not
  reached its end of life is supported, and a version is dropped in the first
  minor release after its end-of-life date.
- ``run_all(delay_seconds)`` only waits between jobs, not after the last one.
- Calling ``run_pending()`` on the same scheduler from several threads no
  longer runs a due job more than once (#630).
- Document sub-second intervals, running a job immediately, and choosing the
  weekday by name.
- Add a security policy (``SECURITY.md``) with private vulnerability
  reporting. Releases are built by a hardened pipeline: pinned GitHub Actions
  and runner images, no build caches, and continuous scanning with CodeQL,
  zizmor and OpenSSF Scorecard.

1.3.1 (2026-10-10)
++++++++++++++++++

- List the schedule-ng maintainer as the package author on PyPI, instead of
  the original author of schedule. Daniel Bader remains credited as the
  original author and copyright holder.
- Point the documentation's links and issue tracker at schedule-ng.

1.3.0 (2026-10-10)
++++++++++++++++++

First release of schedule-ng, a maintained fork of schedule 1.2.2.

- Rename the distribution to ``schedule-ng`` and the package to ``schedule_ng``.
  The API and the ``"schedule"`` logger name are unchanged.
- Require Python 3.9 or newer; test on Python 3.9 to 3.14 (including free-threaded 3.14t)
  on Linux, macOS and Windows.
- ``.at()`` accepts any ``tzinfo`` object for its timezone, such as
  ``zoneinfo.ZoneInfo`` or ``datetime.timezone``, not only pytz timezones.
  Timezone names no longer require pytz: they are looked up with pytz if it is
  installed, and with ``zoneinfo`` otherwise.
- Make the test suite run on Windows.
- Replace setup.py, setup.cfg and tox with a single pyproject.toml.

Issue and pull request numbers below refer to the original
`dbader/schedule <https://github.com/dbader/schedule>`_ repository.

Bug fixes:

- ``every(0)`` and negative intervals raise ``ScheduleValueError`` instead of
  hanging forever (#658). Thanks @oyeong011!
- A rejected ``.at()`` or ``.until()`` call no longer changes the job (#659).
  Thanks @rupayon123!
- ``repr()`` of a job with interval 1 and no unit no longer crashes (#646, #652,
  #651). Thanks Hiren and Friday!
- ``str(job)`` includes the ``.at()`` time, so jobs at different times can be
  told apart (#635, #663). Thanks @BP202302!
- ``.until()`` accepts timezone-aware datetimes (#657). Thanks Kotesh Kumar
  Yelamati!
- ``every(1.0).to(2.0)`` no longer raises ``TypeError`` on Python 3.12+ (#593).
- Calling ``.do()`` twice on a job no longer registers it twice (#215, #305).
- Fix two misleading error messages: an unfilled ``{}`` for invalid hours, and
  "latest is greater than interval" when it was smaller.
- Don't call ``str()`` on jobs in debug log calls (#632). Thanks @fahhem!
- Add a regression test for midnight timezone jobs (#664). Thanks @salpenr!

Fixes for daylight saving time (DST) changes:

- Interval jobs (seconds, minutes, hours) no longer pause for an hour when
  clocks go back (#636, #649). These intervals now measure elapsed time, so
  ``every(4).hours`` is always 4 real hours. **Behaviour change:** schedule
  1.2.2 used wall-clock time, so a job created at midnight on a DST day now
  runs at 05:00 or 03:00 instead of 04:00.
- Jobs with a timezone (``.at("01:30", "UTC")``) no longer run an hour early
  and then on every poll when the local clock goes back.
- Jobs with a timezone no longer run twice the day after their ``.at()`` time
  fell into a DST gap.
- Daily and weekly jobs without a timezone now handle DST gaps like jobs with
  a timezone: a job at 02:30 runs at 03:30 when clocks jump from 02:00 to
  03:00. Previously it ran at 03:00.
- ``idle_seconds`` is correct across DST changes.

``Job.next_run`` is still a naive datetime in local time; jobs now track the
next run in UTC internally.

1.2.2 (2024-05-25)
++++++++++++++++++

- Fix bugs in cross-timezone scheduling (#601, #602, #604, #623)
- Add support for python 3.12 (#606)
- Remove dependency on old mock (#622) Thanks @a-detiste!


1.2.1 (2023-11-01)
++++++++++++++++++

-  Fix bug where schedule was off when using .at with timezone (#583) Thanks @AnezeR!


1.2.0 (2023-04-10)
++++++++++++++++++

- Dropped support for Python 3.6, add support for Python 3.10 and 3.11.
- Add timezone support for .at(). See #517. Thanks @chrimaho!
- Get next run by tag (#463) Thanks @jweijers!
- Add py.typed file. See #521. Thanks @Akuli!

- Fix the re pattern of the 'days'. See #506 Thanks @sunpro108!
- Fix test_until_time failure when run early. See #563. Thanks @emollier!
- Fix crash repr on partially constructed job. See #569. Thanks @CPickens42!
- Code cleanup and modernization. See #567, #536. Thanks @masa-08 and @SergBobrovsky!
- Documentation improvements and fix typos. See #469, #479, #493, #519, #520. Thanks to @NaelsonDouglas, @chrimaho, @rudSarkar

1.1.0 (2021-04-09)
++++++++++++++++++

- Added @repeat() decorator. See #148. Thanks @rhagenaars!
- Added execute .until(). See #195. Thanks @fredthomsen!
- Added job retrieval filtered by tags using get_jobs('tag'). See #419. Thanks @skenvy!
- Added type annotations. See #427. Thanks @martinthoma!

- Bugfix: str() of job when there is no __name__. See #430. Thanks @biggerfisch!
- Improved error messages. See #280, #439. Thanks @connorskees and @sosolidkk!
- Improved logging. See #193. Thanks @zcking!
- Documentation improvements and fix typos. See #424, #435, #436, #453, #437, #448. Thanks @ebllg!

1.0.0 (2021-01-20)
++++++++++++++++++

Depending on your configuration, the following bugfixes might change schedule's behaviour:

- Fix: idle_seconds crashes when no jobs are scheduled. See #401. Thanks @yoonghm!
- Fix: day.at('HH:MM:SS') where HMS=now+10s doesn't run today. See #331. Thanks @qmorek!
- Fix: hour.at('MM:SS'), the seconds are set to 00. See #290. Thanks @eladbi!
- Fix: Long-running jobs skip a day when they finish in the next day #404. Thanks @4379711!

Other changes:

- Dropped Python 2.7 and 3.5 support, added 3.8 and 3.9 support. See #409
- Fix RecursionError when the job is passed to the do function as an arg. See #190. Thanks @connorskees!
- Fix DeprecationWarning of 'collections'. See #296. Thanks @gaguirregabiria!
- Replaced Travis with Github Actions for automated testing
- Revamp and extend documentation. See #395
- Improved tests. Thanks @connorskees and @Jamim!
- Changed log messages to DEBUG level. Thanks @aisk!


0.6.0 (2019-01-20)
++++++++++++++++++

- Make at() accept timestamps with 1 second precision (#267). Thanks @NathanWailes!
- Introduce proper exception hierarchy (#271). Thanks @ConnorSkees!


0.5.0 (2017-11-16)
++++++++++++++++++

- Keep partially scheduled jobs from breaking the scheduler (#125)
- Add support for random intervals (Thanks @grampajoe and @gilbsgilbs)


0.4.3 (2017-06-10)
++++++++++++++++++

- Improve docs & clean up docstrings


0.4.2 (2016-11-29)
++++++++++++++++++

- Publish to PyPI as a universal (py2/py3) wheel


0.4.0 (2016-11-28)
++++++++++++++++++

- Add proper HTML (Sphinx) docs available at https://schedule.readthedocs.io/
- CI builds now run against Python 2.7 and 3.5 (3.3 and 3.4 should work fine but are untested)
- Fixed an issue with ``run_all()`` and having more than one job that deletes itself in the same iteration. Thanks @alaingilbert.
- Add ability to tag jobs and to cancel jobs by tag. Thanks @Zerrossetto.
- Improve schedule docs. Thanks @Zerrossetto.
- Additional docs fixes by @fkromer and @yetingsky.

0.3.2 (2015-07-02)
++++++++++++++++++

- Fixed issues where scheduling a job with a functools.partial as the job function fails. Thanks @dylwhich.
- Fixed an issue where scheduling a job to run every >= 2 days would cause the initial execution to happen one day early. Thanks @WoLfulus for identifying this and providing a fix.
- Added a FAQ item to describe how to schedule a job that runs only once.

0.3.1 (2014-09-03)
++++++++++++++++++

- Fixed an issue with unicode handling in setup.py that was causing trouble on Python 3 and Debian (https://github.com/dbader/schedule/issues/27). Thanks to @waghanza for reporting it.
- Added an FAQ item to describe how to deal with job functions that throw exceptions. Thanks @mplewis.

0.3.0 (2014-06-14)
++++++++++++++++++

- Added support for scheduling jobs on specific weekdays. Example: ``schedule.every().tuesday.do(job)`` or ``schedule.every().wednesday.at("13:15").do(job)`` (Thanks @abultman.)
- Run tests against Python 2.7 and 3.4. Python 3.3 should continue to work but we're not actively testing it on CI anymore.

0.2.1 (2013-11-20)
++++++++++++++++++

- Fixed history (no code changes).

0.2.0 (2013-11-09)
++++++++++++++++++

- This release introduces two new features in a backwards compatible way:
- Allow jobs to cancel repeated execution: Jobs can be cancelled by calling ``schedule.cancel_job()`` or by returning ``schedule.CancelJob`` from the job function. (Thanks to @cfrco and @matrixise.)
- Updated ``at_time()`` to allow running jobs at a particular time every hour. Example: ``every().hour.at(':15').do(job)`` will run ``job`` 15 minutes after every full hour. (Thanks @mattss.)
- Refactored unit tests to mock ``datetime`` in a cleaner way. (Thanks @matts.)

0.1.11 (2013-07-30)
+++++++++++++++++++

- Fixed an issue with ``next_run()`` throwing a ``ValueError`` exception when the job queue is empty. Thanks to @dpagano for pointing this out and thanks to @mrhwick for quickly providing a fix.

0.1.10 (2013-06-07)
+++++++++++++++++++

- Fixed issue with ``at_time`` jobs not running on the same day the job is created (Thanks to @mattss)

0.1.9 (2013-05-27)
++++++++++++++++++

- Added ``schedule.next_run()``
- Added ``schedule.idle_seconds()``
- Args passed into ``do()`` are forwarded to the job function at call time
- Increased test coverage to 100%


0.1.8 (2013-05-21)
++++++++++++++++++

- Changed default ``delay_seconds`` for ``schedule.run_all()`` to 0 (from 60)
- Increased test coverage

0.1.7 (2013-05-20)
++++++++++++++++++

- API change: renamed ``schedule.run_all_jobs()`` to ``schedule.run_all()``
- API change: renamed ``schedule.run_pending_jobs()`` to ``schedule.run_pending()``
- API change: renamed ``schedule.clear_all_jobs()`` to ``schedule.clear()``
- Added ``schedule.jobs``

0.1.6 (2013-05-20)
++++++++++++++++++

- Fix packaging
- README fixes

0.1.4 (2013-05-20)
++++++++++++++++++

- API change: renamed ``schedule.tick()`` to ``schedule.run_pending_jobs()``
- Updated README and ``setup.py`` packaging

0.1.0 (2013-05-19)
++++++++++++++++++

- Initial release

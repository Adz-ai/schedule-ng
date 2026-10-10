schedule-ng
===========

.. image:: https://github.com/Adz-ai/schedule-ng/actions/workflows/ci.yml/badge.svg
        :target: https://github.com/Adz-ai/schedule-ng/actions/workflows/ci.yml

.. image:: https://img.shields.io/pypi/v/schedule-ng.svg
        :target: https://pypi.org/project/schedule-ng/

.. image:: https://readthedocs.org/projects/schedule-ng/badge/?version=latest
        :target: https://schedule-ng.readthedocs.io

.. image:: https://api.scorecard.dev/projects/github.com/Adz-ai/schedule-ng/badge
        :target: https://scorecard.dev/viewer/?uri=github.com/Adz-ai/schedule-ng

Python job scheduling for humans. Run Python functions (or any other callable) periodically using a friendly syntax.

**schedule-ng is a maintained, drop-in compatible fork of** `schedule <https://github.com/dbader/schedule>`_
**by Daniel Bader**, which has not had a release since 1.2.2 (May 2024). The API is unchanged: existing code
keeps working by changing one import.

- A simple to use API for scheduling jobs, made for humans.
- In-process scheduler for periodic jobs. No extra processes needed!
- Very lightweight and no external dependencies.
- Excellent test coverage.
- Tested on Python 3.11 to 3.15 on Linux, macOS and Windows, including free-threaded builds.

Usage
-----

.. code-block:: bash

    $ pip install schedule-ng

.. code-block:: python

    import schedule_ng as schedule
    import time

    def job():
        print("I'm working...")

    schedule.every(10).seconds.do(job)
    schedule.every(10).minutes.do(job)
    schedule.every().hour.do(job)
    schedule.every().day.at("10:30").do(job)
    schedule.every(5).to(10).minutes.do(job)
    schedule.every().monday.do(job)
    schedule.every().wednesday.at("13:15").do(job)
    schedule.every().day.at("12:42", "Europe/Amsterdam").do(job)
    schedule.every().minute.at(":17").do(job)

    def job_with_argument(name):
        print(f"I am {name}")

    schedule.every(10).seconds.do(job_with_argument, name="Peter")

    while True:
        schedule.run_pending()
        time.sleep(1)

Documentation
-------------

schedule-ng's documentation lives at `schedule-ng.readthedocs.io <https://schedule-ng.readthedocs.io>`_.

Migrating from schedule
-----------------------

1. Replace ``schedule`` with ``schedule-ng`` in your dependencies.
2. Replace ``import schedule`` with ``import schedule_ng as schedule``.

Behaviour, exceptions and the ``"schedule"`` logger name are unchanged. Any behavioural fix is listed in the
`changelog <https://github.com/Adz-ai/schedule-ng/blob/main/HISTORY.rst>`_.

Why a fork?
-----------

``schedule`` is used by millions of projects every month, but issues and pull requests have gone unanswered
since 2024. This fork exists to keep it working on new Python versions, fix long-standing bugs and review the
community's pull requests, while keeping what made ``schedule`` popular: a small, simple, dependency-free API.

If the original project becomes active again, this fork will happily contribute its fixes back upstream.

Meta
----

Maintained by Adarssh Athithan. ``schedule`` was originally created by Daniel Bader. Thanks to him, Sijmen Huizenga
and everyone listed in `AUTHORS.rst <https://github.com/Adz-ai/schedule-ng/blob/main/AUTHORS.rst>`_ for their work on it.

Please report problems with schedule-ng in `its issue tracker <https://github.com/Adz-ai/schedule-ng/issues>`_,
not to the original project.

Inspired by `Adam Wiggins' <https://github.com/adamwiggins>`_ article `"Rethinking Cron" <https://adam.herokuapp.com/past/2010/4/13/rethinking_cron/>`_ and the `clockwork <https://github.com/Rykian/clockwork>`_ Ruby module.

Distributed under the MIT license. See `LICENSE.txt <https://github.com/Adz-ai/schedule-ng/blob/main/LICENSE.txt>`_ for more information.

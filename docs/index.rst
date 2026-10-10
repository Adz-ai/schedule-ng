schedule-ng
===========


.. image:: https://github.com/Adz-ai/schedule-ng/actions/workflows/ci.yml/badge.svg
        :target: https://github.com/Adz-ai/schedule-ng/actions/workflows/ci.yml

.. image:: https://img.shields.io/pypi/v/schedule-ng.svg
        :target: https://pypi.org/project/schedule-ng/

Python job scheduling for humans. Run Python functions (or any other callable) periodically using a friendly syntax.

- A simple to use API for scheduling jobs, made for humans.
- In-process scheduler for periodic jobs. No extra processes needed!
- Very lightweight and no external dependencies.
- Excellent test coverage.
- Tested on Python 3.11 to 3.15 on Linux, macOS and Windows.


:doc:`Example <examples>`
-------------------------

.. code-block:: bash

    $ pip install schedule-ng

.. code-block:: python

    import schedule_ng as schedule
    import time

    def job():
        print("I'm working...")

    schedule.every(10).minutes.do(job)
    schedule.every().hour.do(job)
    schedule.every().day.at("10:30").do(job)
    schedule.every().monday.do(job)
    schedule.every().wednesday.at("13:15").do(job)
    schedule.every().day.at("12:42", "Europe/Amsterdam").do(job)
    schedule.every().minute.at(":17").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)


More :doc:`examples`

When **not** to use Schedule
----------------------------
Let's be honest, Schedule is not a 'one size fits all' scheduling library.
This library is designed to be a simple solution for simple scheduling problems.
You should probably look somewhere else if you need:

* Job persistence (remember schedule between restarts)
* Exact timing (sub-second precision execution)
* Concurrent execution (multiple threads)
* Localization (workdays or holidays)


**Schedule does not account for the time it takes for the job function to execute.**
To guarantee a stable execution schedule you need to move long-running jobs off the main-thread (where the scheduler runs).
See :doc:`parallel-execution` for a sample implementation.


Read More
---------
.. toctree::
   :maxdepth: 2

   installation
   examples
   background-execution
   parallel-execution
   timezones
   exception-handling
   logging
   multiple-schedulers
   faq
   reference
   development

.. toctree::
   :maxdepth: 1

   changelog


Issues
------

If you encounter any problems, please `file an issue <https://github.com/Adz-ai/schedule-ng/issues>`_ along with a detailed description.
Please also use the search feature in the issue tracker beforehand to avoid creating duplicates. Thank you 😃

About Schedule
--------------

schedule-ng is a maintained fork of `schedule <https://github.com/dbader/schedule>`_, originally created by Daniel Bader.

Inspired by `Adam Wiggins' <https://github.com/adamwiggins>`_ article `"Rethinking Cron" <https://adam.herokuapp.com/past/2010/4/13/rethinking_cron/>`_ and the `clockwork <https://github.com/Rykian/clockwork>`_ Ruby module.


Distributed under the MIT license. See ``LICENSE.txt`` for more information.

.. include:: ../AUTHORS.rst

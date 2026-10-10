Frequently Asked Questions
==========================

Frequently asked questions on the usage of schedule.
Did you get here using an 'old' link and expected to see more questions?

AttributeError: 'module' object has no attribute 'every'
--------------------------------------------------------

I'm getting

.. code-block:: text

    AttributeError: 'module' object has no attribute 'every'

when I try to use schedule.

This happens if your code imports the wrong ``schedule`` module.
Make sure you don't have a ``schedule.py`` file in your project that overrides the ``schedule`` module provided by this library.


ModuleNotFoundError: No module named 'schedule'
-----------------------------------------------

It seems python can't find the schedule package. Let's check some common causes.

Did you install schedule? If not, follow :doc:`installation`. Validate installation:

* Did you install using pip? Run ``pip3 list | grep schedule``. This should return ``schedule   0.6.0`` (or a higher version number)
* Did you install using apt? Run ``dpkg -l | grep python3-schedule``. This should return something along the lines of ``python3-schedule     0.3.2-1.1     Job scheduling for humans (Python 3)`` (or a higher version number)

Are you used python 3 to install Schedule, and are running the script using python 3?
For example, if you installed schedule using a version of pip that uses Python 2, and your code runs in Python 3, the package won't be found.
In this case the solution is to install Schedule using pip3: ``pip3 install schedule``.

Are you using virtualenv? Check that you are running the script inside the same virtualenv where you installed schedule.

Is this problem occurring when running the program from inside and IDE like PyCharm or VSCode?
Try to run your program from a commandline outside of the IDE.
If it works there, the problem is with your IDE configuration.
It might be that your IDE uses a different Python interpreter installation.

Still having problems? Use Google and StackOverflow before submitting an issue.

ScheduleValueError: Unknown timezone
------------------------------------

The timezone name passed to ``.at()`` is not known to Python's :mod:`zoneinfo`.
Check the spelling against the `list of timezone names <https://en.wikipedia.org/wiki/List_of_tz_database_time_zones>`_.
On Windows, install the `tzdata <https://pypi.org/project/tzdata/>`_ package: ``pip install tzdata``.
pytz is no longer required for timezones.

Can I schedule jobs more often than every second?
-------------------------------------------------
Yes, intervals can be floats: ``schedule.every(0.25).seconds``. See :doc:`Examples <examples>`.

Can I run a job right away, and then on its schedule?
-----------------------------------------------------
Yes, call ``run()`` on the job. See :doc:`Examples <examples>`.

Does schedule support time zones?
---------------------------------
Yes! See :doc:`Timezones <timezones>`.

What if my task throws an exception?
------------------------------------
See :doc:`Exception Handling <exception-handling>`.

How can I run a job only once?
------------------------------
See :doc:`Examples <examples>`.

How can I cancel several jobs at once?
--------------------------------------
See :doc:`Examples <examples>`.

How to execute jobs in parallel?
--------------------------------
See :doc:`Parallel Execution <parallel-execution>`.

How to continuously run the scheduler without blocking the main thread?
-----------------------------------------------------------------------
:doc:`Background Execution<background-execution>`.

Another question?
-----------------
If you are left with an unanswered question, `browse the issue tracker <https://github.com/Adz-ai/schedule-ng/issues>`_ to see if your question has been asked before.
Feel free to create a new issue if that's not the case. Thank you 😃
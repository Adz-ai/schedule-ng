Timezone & Daylight Saving Time
===============================

Timezone in .at()
~~~~~~~~~~~~~~~~~

Schedule supports setting the job execution time in another timezone using the ``.at`` method.

Timezones are only available in the ``.at`` function, like so:

.. code-block:: python

    # Pass a timezone name
    schedule.every().day.at("12:42", "Europe/Amsterdam").do(job)

    # Pass any tzinfo object, such as a zoneinfo timezone
    from zoneinfo import ZoneInfo
    schedule.every().friday.at("12:42", ZoneInfo("Africa/Lagos")).do(job)

Timezone names are looked up with `pytz <https://pypi.org/project/pytz/>`_ if it is installed,
and with Python's built-in :mod:`zoneinfo` otherwise.
On Windows, zoneinfo needs the `tzdata <https://pypi.org/project/tzdata/>`_ package:

.. code-block:: bash

    pip install tzdata

Schedule uses the timezone to calculate the next run.
``next_run`` and ``last_run`` are `naive <https://docs.python.org/3/library/datetime.html>`_ datetimes
in Python's local timezone.

Daylight Saving Time
~~~~~~~~~~~~~~~~~~~~
Intervals in seconds, minutes and hours measure elapsed time.
A job that runs every 4 hours runs every 4 real hours, also when the clock changes.

Days and weeks follow the clock: a job that runs every day at 10:30 runs at 10:30,
in the timezone given to ``.at()`` or in local time.
The rules below apply to both.

Example clock moves forward:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When a job is scheduled in the gap that occurs when the clock moves forward, the job is scheduled after the gap.

A job is scheduled ``.at("02:30", "Europe/Berlin")``.
When the clock moves from ``02:00`` to ``03:00``, the job will run once at ``03:30``.
The day after it will return to normal and run at ``02:30``.

A job is scheduled ``.at("01:00", "Europe/London")``.
When the clock moves from ``01:00`` to ``02:00``, the job will run once at ``02:00``.

Example clock moves backwards:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
A job is scheduled ``.at("02:30", "Europe/Berlin")``.
When the clock moves back from ``03:00`` to ``02:00``, the job will run once at ``02:30``.
It will run only at the first time the clock hits ``02:30``, but not the second time.
The day after, it will return to normal and run at ``02:30``.

Example scheduling across timezones
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Let's say we are in ``Europe/Berlin`` and local datetime is ``2022 march 20, 10:00:00``.
At this moment daylight saving time is not in effect in Berlin (UTC+1).

We schedule a job to run every day at 10:30:00 in America/New_York.
At this time, daylight saving time is in effect in New York (UTC-4).

.. code-block:: python

    s = every().day.at("10:30", "America/New_York").do(job)

Because of the 5 hour time difference between Berlin and New York the job should effectively run at ``15:30:00``.
So the next run in Berlin time is ``2022 march 20, 15:30:00``:

.. code-block:: python

    print(s.next_run)
    # 2022-03-20 15:30:00

    print(repr(s))
    # Every 1 day at 10:30:00 do job() (last run: [never], next run: 2022-03-20 15:30:00)

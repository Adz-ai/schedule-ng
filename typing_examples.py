"""
Type-checked examples of the public API.

This file is not run; ``mypy`` checks it so the type hints keep matching how
the library is used (see dbader/schedule#559). Each ``assert_type`` documents
an expected type.
"""

import datetime
from collections.abc import Callable
from typing import assert_type
from zoneinfo import ZoneInfo

import schedule_ng as schedule


def job(name: str = "world") -> None:
    print(f"hello {name}")


# Intervals accept floats as well as ints.
assert_type(schedule.every(0.5).seconds.do(job), schedule.Job)
assert_type(schedule.every(1.5).to(3.0).minutes.do(job), schedule.Job)

# Builder chains keep the Job type.
assert_type(schedule.every().monday.at("10:30").do(job, name="Monday"), schedule.Job)
assert_type(
    schedule.every().day.at("10:30", ZoneInfo("Europe/Amsterdam")), schedule.Job
)
assert_type(
    schedule.every().day.at("10:30", "Europe/Amsterdam").tag("daily"), schedule.Job
)
assert_type(schedule.every().hour.until(datetime.timedelta(hours=8)), schedule.Job)
assert_type(schedule.every().weekday.at("09:00").do(job), schedule.Job)
assert_type(schedule.every(5).minutes.weekend, schedule.Job)

# Scheduler-level helpers.
assert_type(schedule.next_run(), datetime.datetime | None)
assert_type(schedule.idle_seconds(), float | None)
assert_type(schedule.get_jobs("daily"), list[schedule.Job])
schedule.run_all(delay_seconds=0.5)


# The decorator keeps the decorated function's signature.
@schedule.repeat(schedule.every(10).minutes, "decorated")
def decorated(name: str) -> int:
    return len(name)


keeps_signature: Callable[[str], int] = decorated
assert_type(decorated("x"), int)


# Subclasses of Job keep their type through the builder chain.
class MyJob(schedule.Job):
    pass


assert_type(MyJob(1, schedule.Scheduler()).seconds.do(job), MyJob)

Installation
============


Python version support
######################

We recommend using the latest version of Python.
schedule-ng is tested on Python 3.11 to 3.15 on Linux, macOS and Windows,
including the free-threaded builds.

schedule-ng supports every Python version that has not reached its
`end of life <https://devguide.python.org/versions/>`_. Support for a version
is dropped in the first minor release after its end-of-life date, never in a
patch release. pip installs the newest release that supports your Python, so
older Python versions keep working with older releases:

=================  ======================
Python             Latest schedule-ng
=================  ======================
3.11 and newer     latest
3.9, 3.10          1.3.1
=================  ======================

For Python 3.8 or older, use the original
`schedule <https://pypi.org/project/schedule/>`_ 1.2.2.


Dependencies
############

schedule-ng has no required dependencies.

Timezone names passed to ``.at()``, such as ``"Europe/Amsterdam"``, are looked up with
`pytz <https://pypi.org/project/pytz/>`_ if it is installed, and with Python's built-in :mod:`zoneinfo` otherwise.
On Windows, zoneinfo needs the `tzdata <https://pypi.org/project/tzdata/>`_ package.

Installation instructions
#########################

Problems? Check out :doc:`faq`.

PIP (preferred)
***************
The recommended way to install this package is to use pip.
Use the following command to install it:

.. code-block:: bash

    $ pip install schedule-ng

Schedule is now installed.
Check out the :doc:`examples </examples>` or go to the :doc:`the documentation overview </index>`.

Migrating from schedule
***********************
schedule-ng is a drop-in replacement for `schedule <https://pypi.org/project/schedule/>`_.
Replace ``schedule`` with ``schedule-ng`` in your dependencies, and ``import schedule``
with ``import schedule_ng as schedule`` in your code.

The Linux distribution and conda packages named ``schedule`` contain the original
library, not schedule-ng.

Install manually
****************
If you don't have access to a package manager or need more control, you can manually copy the library into your project.
This is easy as the library consists of a single MIT-licensed source file.
However, this method is highly discouraged as you won't receive automatic updates.

1. Go to the `GitHub repo <https://github.com/Adz-ai/schedule-ng>`_.
2. Open the file `schedule_ng/__init__.py` and copy the code.
3. In your project, create a package named `schedule_ng` and paste the code in a file named `__init__.py`.

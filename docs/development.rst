Development
===========

These instructions are geared towards people who want to help develop this library.

Preparing for development
-------------------------
The project uses `uv <https://docs.astral.sh/uv/>`_ to manage its development environment.
After installing uv, clone the repository; uv installs everything else on first use.

.. code-block:: bash

    git clone https://github.com/Adz-ai/schedule-ng.git
    cd schedule-ng


Running tests
-------------

Run the tests with coverage:

.. code-block:: bash

    uv run pytest --cov --cov-report=term-missing

The tests run on Linux, macOS and Windows. Tests that need pytz are skipped
when it is not installed; CI runs the suite both with and without it.

Linting, formatting and type checking
-------------------------------------
This project uses `ruff <https://docs.astral.sh/ruff/>`_ and `mypy <https://mypy-lang.org/>`_:

.. code-block:: bash

    uv run ruff check
    uv run ruff format
    uv run mypy

Compiling documentation
-----------------------

The documentation is written in `reStructuredText <https://docutils.sourceforge.io/rst.html>`_
and built with `Sphinx <https://www.sphinx-doc.org/>`_ using the `alabaster <https://alabaster.readthedocs.io/en/latest/>`_ theme:

.. code-block:: bash

    uv run --only-group docs --with-editable . sphinx-build -W -b html docs docs/_build/html

The resulting html can be found in ``docs/_build/html``.

Publish a new version
---------------------

1. Update ``HISTORY.rst`` and ``AUTHORS.rst``.
2. Bump ``__version__`` in ``schedule_ng/__init__.py`` and ``release`` in ``docs/conf.py``.
3. Merge these changes into ``main`` and wait for CI to pass.
4. Tag and push the release:

   .. code-block:: bash

       git tag -a vX.Y.Z -m "schedule-ng X.Y.Z"
       git push origin vX.Y.Z

5. Approve the deployment to the ``pypi`` environment in the GitHub Actions run.
   The release workflow publishes to PyPI using trusted publishing, then creates
   the GitHub release with the files signed by Sigstore.

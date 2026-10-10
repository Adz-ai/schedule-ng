# Security policy

## Supported versions

Security fixes are released for the latest minor version of schedule-ng.
Please upgrade to the latest release before reporting a problem.

## Reporting a vulnerability

Please **don't open a public issue** for security problems.

Report them privately through GitHub instead:
[Report a vulnerability](https://github.com/Adz-ai/schedule-ng/security/advisories/new).

Include what you found, how to reproduce it, and which versions are affected.
You can expect an acknowledgement within 7 days. Once a fix is released, the
advisory is published and you are credited, unless you prefer not to be.

## Good to know

- schedule-ng has no runtime dependencies and does no network or file I/O.
- Jobs run with the permissions of your process. Only schedule functions you trust.
- Schedulers and jobs can be pickled. As with any pickle, only unpickle data
  from a source you trust: unpickling untrusted data can run arbitrary code.
- Releases are published from GitHub Actions with
  [trusted publishing](https://docs.pypi.org/trusted-publishers/) and include
  [attestations](https://docs.pypi.org/attestations/), so you can verify that a
  release was built from this repository.

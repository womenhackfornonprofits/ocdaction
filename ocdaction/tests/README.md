## OCD Action Django App

Our tests package: `ocdaction.tests` is a valid Django app and should
be installed in Django's `INSTALLED_APPS` setting during test suite runs.

## Test Placement

The tests folder is laid out in such a way that it mirrors as closely as
possible the actual codebase.

### Example

Here is an example to show you how new test files should be placed:

    `ocdaction/apps/profiles/example_file.py`

is tested at:

    `ocdaction/tests/apps/profiles/test_example_file.py`

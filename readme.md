Welcome to ServerCheck
======================

Theoretical discussions are all fair and good, but the main objective of the
whole discourse is to encourage people to *actually do testing*.

To realize testing at Schnapptack I wrote a small python script that is going to
be hooked to a Jenkins service which executes it each few hours.

The script uses the response library to check our servers for their status.
If they don't return a 200, the sysadmin gets a notification.

Installation:
-------------

ServerCheck comes as a Python package. It is installed by running the included
setup-script. To do so, issue
``python setup.py develop``
into your shell. This installs the package. Next you need to install the
dependencies from the requirements.txt into your venv. Do this by issuing
``pip install -r requirements.txt``.
Now you're set.

You may now run your test with the predefined URLs by issuing
``python tests/tests.py``
into the terminal which will run the test.

Each dot the terminal returns marks a passed test, a F marks a failed test.
Failed tests will also throw an exception which can be helpful to debug the
whole thing.


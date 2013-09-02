Example Robot Framework test
============================

With the robot framework plain text syntax, a minimal test suite
would consists of ``*** test cases ***`` header and at least
one test case, like:

.. code:: robotframework

   *** Settings ***

   Library  Selenium2Library

   Suite teardown  Close all browsers

one ``*** test cases ***``-header may be followed by as many
tests as required, like:

.. code:: robotframework

   *** test cases ***

   Take screenshot of pypi
       Open browser  http://pypi.python.org/pypi/
       Capture page screenshot  pypi.png

And this documentation can include the captured screenshots:

.. image:: pypi.png

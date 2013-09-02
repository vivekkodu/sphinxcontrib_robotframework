Example Robot Framework test
============================

With the robot framework plain text syntax, a minimal test suite
would consists of ``*** test cases ***`` header and at least
one test case, like:

.. code:: robotframework

   *** Settings ***

   Resource  third_setup.robot

   Suite Teardown  Close all browsers


one ``*** test cases ***``-header may be followed by as many
tests as required, like:

.. code:: robotframework

   *** test cases ***

   Take screenshot of Google
       Open browser  http://google.com/
       Capture page screenshot  google.png

And this documentation can include the captured screenshots:

.. image:: google.png

Example Robot Framework test
============================

With the robot framework plain text syntax, a minimal test suite
would consists of ``*** test cases ***`` header and at least
one test case, like:

.. code:: robotframework

   *** test cases ***

   foo is always foo
       should be equal  foo  foo

one ``*** test cases ***``-header may be followed by as many
tests as required, like:

.. code:: robotframework

   *** test cases ***

   foo is still foo
       should be equal  foo  foo

   foo is never bar
       should not be equal  foo  bar

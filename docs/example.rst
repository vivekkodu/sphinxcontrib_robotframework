Document with embedded tests
============================

With the Robot Framework space separated format, a minimal test suite
would consists of ``*** Test Cases ***`` header and at least
one test case, like:

.. code:: robotframework

   *** Test Cases ***

   Foo is always foo
       Should be equal  foo  foo

One ``*** Test Cases ***``-header may be followed by as many
tests as required, like:

.. code:: robotframework

   *** Test Cases ***

   Foo is still foo
       Should be equal  foo  foo

   Foo is never bar
       Should not be equal  foo  bar

Your first Robot Framework doctest
==================================

With the Robot Framework plain text syntax, a minimal test suite
would consists of ``*** Test Cases ***`` header and at least
one test case, like:

.. code:: robotframework

   *** Test Cases ***

   Foo is always Foo
       Should be equal  Foo  Foo

One ``*** Test Cases ***``-header may be followed by as many
tests as required, like:

.. code:: robotframework

   *** Test Cases ***

   Foo is still Foo
       Should be equal  Foo  Foo

   Foo is never Bar
       Should not be equal  Foo  Bar

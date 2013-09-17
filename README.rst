Sphinx-extension for Robot Framework
====================================

``sphinxcontrib_robotframework`` is a Sphinx-extensions, which executes
embedded Robot Framework -tests during Sphinx-documentation compilation.

Usage
-----

Add the following lines into your Sphinx-project's ``conf.py``::

    extensions = ['sphinxcontrib_robotframework']

    sphinxcontrib_robotframework_enabled = True

Write your Robot Framework tests with space separated syntax into Docutils'
``code``-directives with ``robotframework``-language, like::

    .. code:: robotframework

       *** Test cases ***

       ...

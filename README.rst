pytest-memory-usage
===================================

.. image:: https://travis-ci.org/eli-b/pytest-memory-usage.svg?branch=master
    :target: https://travis-ci.org/eli-b/pytest-memory-usage
    :alt: See Build Status on Travis CI

.. image:: https://ci.appveyor.com/api/projects/status/github/eli-b/pytest-memory-usage?branch=master
    :target: https://ci.appveyor.com/project/eli-b/pytest-memory-usage/branch/master
    :alt: See Build Status on AppVeyor

Reports test memory usage, and adds memory bounds

----

This `Pytest`_ plugin was generated with `Cookiecutter`_ along with `@hackebrot`_'s `Cookiecutter-pytest-plugin`_ template.


Features
--------

* Reports the memory usage of each test
* Plots the memory usage of the test suite
* Calls gc.collect() when the memory usage passes the soft memory limit
* Terminates the test suite when the hard memory limit


Requirements
------------

* psutil


Installation
------------

You can install "pytest-memory-usage" via `pip`_ from `PyPI`_::

    $ pip install pytest-memory-usage


Usage
-----

* TODO

Note: teardown_class memory_usage is not reported.

Contributing
------------
Contributions are very welcome. Tests can be run with `tox`_, please ensure
the coverage at least stays the same before you submit a pull request.

License
-------

Distributed under the terms of the `GNU GPL v3.0`_ license, "pytest-memory-usage" is free and open source software


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`@hackebrot`: https://github.com/hackebrot
.. _`MIT`: http://opensource.org/licenses/MIT
.. _`BSD-3`: http://opensource.org/licenses/BSD-3-Clause
.. _`GNU GPL v3.0`: http://www.gnu.org/licenses/gpl-3.0.txt
.. _`Apache Software License 2.0`: http://www.apache.org/licenses/LICENSE-2.0
.. _`cookiecutter-pytest-plugin`: https://github.com/pytest-dev/cookiecutter-pytest-plugin
.. _`file an issue`: https://github.com/eli-b/pytest-memory-usage/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`tox`: https://tox.readthedocs.io/en/latest/
.. _`pip`: https://pypi.python.org/pypi/pip/
.. _`PyPI`: https://pypi.python.org/pypi

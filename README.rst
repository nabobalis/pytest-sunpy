============
pytest-sunpy
============

This is a meta-package that pulls in the dependencies that are used by `SunPy`_'s test suite.

.. _SunPy: https://sunpy.org/

Dependencies
------------

The following dependencies are installed by this package:

* The `pytest-astropy`_ meta-package for testing. This pulls in:
    * `pytest`_ testing framework for Python.
    * `pytest-remotedata`_, a ``pytest`` plugin used for controlling access to data files hosted online.
    * `pytest-doctestplus`_, a ``pytest`` plugin that provides advanced features for testing example code in documentation.
    * `pytest-openfiles`_, a ``pytest`` plugin for detecting file handles that were inadvertently left open at the end of unit tests.
    * `pytest-arraydiff`_, a ``pytest`` plugin that enables the generation and comparison of data arrays produced during unit tests.
* The `hypothesis`_ framework for property based testing.
* The `pytest-cov`_ a ``pytest`` plugin that produces coverage reports.
* The `pytest-mock`_ a ``pytest`` plugin that is a thin-wrapper around the mock package for easier use with py.test.
* The `pytest-rerunfailures`_ a ``pytest`` plugin that re-runs failed tests up to -n times to eliminate flakey failures.
* The `pytest-xdist`_ a ``pytest`` plugin that allows parallel test processes.

.. _pytest: https://docs.pytest.org/en/latest/
.. _pytest-astropy: https://github.com/astropy/pytest-astropy
.. _pytest-remotedata: https://github.com/astropy/pytest-remotedata
.. _pytest-doctestplus: https://github.com/astropy/pytest-doctestplus
.. _pytest-openfiles: https://github.com/astropy/pytest-openfiles
.. _pytest-arraydiff: https://github.com/astrofrog/pytest-arraydiff
.. _hypothesis: https://hypothesis.readthedocs.io/en/latest/
.. _pytest-cov: https://pypi.org/project/pytest-cov/
.. _pytest-mock: https://github.com/pytest-dev/pytest-mock
.. _pytest-rerunfailures: https://github.com/pytest-dev/pytest-rerunfailures
.. _pytest-xdist: https://pypi.org/project/pytest-xdist/

Installation
------------

The ``pytest-sunpy`` plugin can be installed using ``pip``::

    $ pip install pytest-sunpy

It is also possible to install the latest development version from the source repository::

    $ git clone https://github.com/sunpy/pytest-sunpy
    $ cd pytest-sunpy
    $ pip install -e .

In either case, the plugin will automatically be registered for use with ``pytest``.

Development Status
------------------

Questions, bug reports, and feature requests can be submitted on `GitHub`_.

.. _GitHub: https://github.com/sunpy/pytest-sunpy

License
-------
This package is licensed under a 3-clause BSD style license - see the
``LICENSE.rst`` file.

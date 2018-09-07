============
pytest-sunpy
============

This is a meta-package that pulls in the dependencies that are used by
`SunPy`_.

.. _SunPy: https://sunpy.org/

Dependencies
------------

The following dependencies are installed by this package:

* The `pytest`_ testing framework for Python
* `pytest-remotedata`_, a ``pytest`` plugin used for controlling access to data
  files hosted online
* `pytest-doctestplus`_, a ``pytest`` plugin that provides advanced features
  for testing example code in documentation
* `pytest-openfiles`_, a ``pytest`` plugin for detecting file handles that were
  inadvertently left open at the end of unit tests
* `pytest-arraydiff`_, a ``pytest`` plugin that enables the generation and
  comparison of data arrays produced during unit tests

.. _pytest: https://doc.pytest.org
.. _pytest-remotedata: https://github.com/astropy/pytest-remotedata
.. _pytest-doctestplus: https://github.com/astropy/pytest-doctestplus
.. _pytest-openfiles: https://github.com/astropy/pytest-openfiles
.. _pytest-arraydiff: https://github.com/astrofrog/pytest-arraydiff

Installation
------------

The ``pytest-sunpy`` plugin can be installed using ``pip``::

    $ pip install pytest-sunpy

It is also possible to install the latest development version from the source
repository::

    $ git clone https://github.com/sunpy/pytest-sunpy
    $ cd pytest-sunpy
    $ python ./setup.py install

In either case, the plugin will automatically be registered for use with
``pytest``.

Development Status
------------------

Questions, bug reports, and feature requests can be submitted on `github`_.

.. _github: https://github.com/sunpy/pytest-sunpy

License
-------
This package is licensed under a 3-clause BSD style license - see the
``LICENSE.rst`` file.
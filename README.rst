.. image:: http://www.repostatus.org/badges/latest/active.svg
    :target: http://www.repostatus.org/#active
    :alt: Project Status: Active — The project has reached a stable, usable
          state and is being actively developed.

.. image:: https://travis-ci.com/jwodder/wheel-filename.svg?branch=master
    :target: https://travis-ci.com/jwodder/wheel-filename

.. image:: https://codecov.io/gh/jwodder/wheel-filename/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/jwodder/wheel-filename

.. image:: https://img.shields.io/pypi/pyversions/wheel-filename.svg
    :target: https://pypi.org/project/wheel-filename/

.. image:: https://img.shields.io/github/license/jwodder/wheel-filename.svg
    :target: https://opensource.org/licenses/MIT
    :alt: MIT License

.. image:: https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg
    :target: https://saythanks.io/to/jwodder

`GitHub <https://github.com/jwodder/wheel-filename>`_
| `PyPI <https://pypi.org/project/wheel-filename/>`_
| `Issues <https://github.com/jwodder/wheel-filename/issues>`_
| `Changelog <https://github.com/jwodder/wheel-filename/blob/master/CHANGELOG.md>`_

``wheel-filename`` lets you verify `wheel
<https://www.python.org/dev/peps/pep-0427/>`_ filenames and parse them into
their component fields.  It adheres strictly to the relevant PEPs, except that
version components are allowed to contain ``!`` and ``+`` for full PEP 440
support.

Installation
============
``wheel-filename`` requires Python 3.5 or higher.  Just use `pip
<https://pip.pypa.io>`_ for Python 3 (You have pip, right?) to install
``wheel-filename`` and its dependencies::

    python3 -m pip install wheel-filename


Example
=======

::

    >>> from wheel_filename import parse_wheel_filename
    >>> pwf = parse_wheel_filename('pip-18.0-py2.py3-none-any.whl')
    >>> str(pwf)
    'pip-18.0-py2.py3-none-any.whl'
    >>> pwf.project
    'pip'
    >>> pwf.version
    '18.0'
    >>> pwf.build is None
    True
    >>> pwf.python_tags
    ['py2', 'py3']
    >>> pwf.abi_tags
    ['none']
    >>> pwf.platform_tags
    ['any']
    >>> list(pwf.tag_triples())
    ['py2-none-any', 'py3-none-any']


API
===

``parse_wheel_filename(filename)``
   Parses a wheel filename (without any directory components) and returns a
   ``ParsedWheelFilename`` instance.  If the filename is invalid, raises an
   ``InvalidFilenameError``.

``ParsedWheelFilename``
   A class representing the components of a wheel filename.  It has the
   following attributes and methods:

   ``project``
      The name of the project distributed by the wheel

   ``version``
      The version of the project distributed by the wheel

   ``build``
      The wheel's build tag (`None` if not defined)

   ``python_tags``
      A list of Python tags for the wheel

   ``abi_tags``
      A list of ABI tags for the wheel

   ``platform_tags``
      A list of platform tags for the wheel

   ``str(pwf)``
      Stringifying a ``ParsedWheelFilename`` returns the original filename

   ``tag_triples()``
      Returns an iterator of all simple tag triples formed from the
      compatibility tags in the filename

``InvalidFilenameError``
   A subclass of ``ValueError`` raised when an invalid wheel filename is passed
   to ``parse_wheel_filename()``.  It has a ``filename`` attribute containing
   the invalid filename.

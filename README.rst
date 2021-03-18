.. image:: http://www.repostatus.org/badges/latest/active.svg
    :target: http://www.repostatus.org/#active
    :alt: Project Status: Active — The project has reached a stable, usable
          state and is being actively developed.

.. image:: https://github.com/jwodder/wheel-filename/workflows/Test/badge.svg?branch=master
    :target: https://github.com/jwodder/wheel-filename/actions?workflow=Test
    :alt: CI Status

.. image:: https://codecov.io/gh/jwodder/wheel-filename/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/jwodder/wheel-filename

.. image:: https://img.shields.io/pypi/pyversions/wheel-filename.svg
    :target: https://pypi.org/project/wheel-filename/

.. image:: https://img.shields.io/github/license/jwodder/wheel-filename.svg
    :target: https://opensource.org/licenses/MIT
    :alt: MIT License

`GitHub <https://github.com/jwodder/wheel-filename>`_
| `PyPI <https://pypi.org/project/wheel-filename/>`_
| `Issues <https://github.com/jwodder/wheel-filename/issues>`_
| `Changelog <https://github.com/jwodder/wheel-filename/blob/master/CHANGELOG.md>`_

``wheel-filename`` lets you verify `wheel
<https://www.python.org/dev/peps/pep-0427/>`_ filenames and parse them into
their component fields.

This package adheres strictly to the relevant PEPs, with the following
exceptions:

- Unlike other filename components, version components may contain the
  characters ``!`` and ``+`` for full PEP 440 support.

- Version components may be any sequence of the relevant set of characters;
  they are not verified for PEP 440 compliance.

- The ``.whl`` file extension is matched case-insensitively.


Installation
============
``wheel-filename`` requires Python 3.6 or higher.  Just use `pip
<https://pip.pypa.io>`_ for Python 3 (You have pip, right?) to install
``wheel-filename``::

    python3 -m pip install wheel-filename


Example
=======

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
   Parses a wheel filename (a ``str``, ``bytes``, or ``os.PathLike``) and
   returns a ``ParsedWheelFilename`` instance.  Any leading directory
   components are stripped from the argument before processing.  If the
   filename is not a valid wheel filename, raises an ``InvalidFilenameError``.

``ParsedWheelFilename``
   A namedtuple representing the components of a wheel filename.  It has the
   following attributes and methods:

   ``project: str``
      The name of the project distributed by the wheel

   ``version: str``
      The version of the project distributed by the wheel

   ``build: Optional[str]``
      The wheel's build tag (``None`` if not defined)

   ``python_tags: List[str]``
      A list of Python tags for the wheel

   ``abi_tags: List[str]``
      A list of ABI tags for the wheel

   ``platform_tags: List[str]``
      A list of platform tags for the wheel

   ``str(pwf)``
      Stringifying a ``ParsedWheelFilename`` returns the original filename

   ``tag_triples() -> Iterator[str]``
      Returns an iterator of all simple tag triples formed from the
      compatibility tags in the filename

``InvalidFilenameError``
   A subclass of ``ValueError`` raised when an invalid wheel filename is passed
   to ``parse_wheel_filename()``.  It has a ``filename`` attribute containing
   the basename of the invalid filename.

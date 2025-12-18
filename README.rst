|repostatus| |ci-status| |coverage| |pyversions| |license|

.. |repostatus| image:: https://www.repostatus.org/badges/latest/active.svg
    :target: https://www.repostatus.org/#active
    :alt: Project Status: Active — The project has reached a stable, usable
          state and is being actively developed.

.. |ci-status| image:: https://github.com/wheelodex/wheel-filename/actions/workflows/test.yml/badge.svg
    :target: https://github.com/wheelodex/wheel-filename/actions/workflows/test.yml
    :alt: CI Status

.. |coverage| image:: https://codecov.io/gh/wheelodex/wheel-filename/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/wheelodex/wheel-filename

.. |pyversions| image:: https://img.shields.io/pypi/pyversions/wheel-filename.svg
    :target: https://pypi.org/project/wheel-filename/

.. |license| image:: https://img.shields.io/github/license/wheelodex/wheel-filename.svg
    :target: https://opensource.org/licenses/MIT
    :alt: MIT License

`GitHub <https://github.com/wheelodex/wheel-filename>`_
| `PyPI <https://pypi.org/project/wheel-filename/>`_
| `Issues <https://github.com/wheelodex/wheel-filename/issues>`_
| `Changelog <https://github.com/wheelodex/wheel-filename/blob/master/CHANGELOG.md>`_

``wheel-filename`` lets you verify wheel_ filenames and parse them into their
component fields.

.. _wheel: https://packaging.python.org/en/latest/specifications
           /binary-distribution-format/

This package adheres strictly to the standard, with the following exceptions:

- Version components may be any sequence of the relevant set of characters;
  they are not verified for PEP 440 compliance.

- The ``.whl`` file extension is matched case-insensitively.


Installation
============
``wheel-filename`` requires Python 3.10 or higher.  Just use `pip
<https://pip.pypa.io>`_ for Python 3 (You have pip, right?) to install it::

    python3 -m pip install wheel-filename


Example
=======

>>> from wheel_filename import WheelFilename
>>> pwf = WheelFilename.parse('pip-18.0-py2.py3-none-any.whl')
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

``WheelFilename``
   A dataclass representing the components of a wheel filename.  It has the
   following attributes and methods:

   ``WheelFilename.parse(filename)``
      (classmethod) Parses a wheel filename (a ``str``, ``bytes``, or
      ``os.PathLike``) and returns a ``WheelFilename`` instance.  Any leading
      directory components are stripped from the argument before processing.
      If the filename is not a valid wheel filename, raises a ``ParseError``.

   ``project: str``
      The name of the project distributed by the wheel

   ``version: str``
      The version of the project distributed by the wheel

   ``build: str | None``
      The wheel's build tag (``None`` if not defined)

   ``python_tags: list[str]``
      A list of Python tags for the wheel

   ``abi_tags: list[str]``
      A list of ABI tags for the wheel

   ``platform_tags: list[str]``
      A list of platform tags for the wheel

   ``str(pwf)``
      Stringifying a ``WheelFilename`` returns the original filename

   ``tag_triples() -> Iterator[str]``
      Returns an iterator of all simple tag triples formed from the
      compatibility tags in the filename

``ParseError``
   A subclass of ``ValueError`` raised when an invalid wheel filename is passed
   to ``WheelFilename.parse()``.  It has a ``filename`` attribute containing
   the basename of the invalid filename.


Command
=======

*New in version 1.4.0*

``wheel-filename`` also provides a command of the same name that takes a wheel
filename (The actual wheel does not have to exist) and outputs the filename
components as JSON.

Example::

    $ wheel-filename pip-18.0-py2.py3-none-any.whl
    {
        "project": "pip",
        "version": "18.0",
        "build": null,
        "python_tags": [
            "py2",
            "py3"
        ],
        "abi_tags": [
            "none"
        ],
        "platform_tags": [
            "any"
        ]
    }

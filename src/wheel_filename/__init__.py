"""
Parse wheel filenames

``wheel-filename`` lets you verify wheel_ filenames and parse them into their
component fields.

.. _wheel: https://packaging.python.org/en/latest/specifications
           /binary-distribution-format/

This package adheres strictly to the standard, with the following exceptions:

- Version components may be any sequence of the relevant set of characters;
  they are not verified for PEP 440 compliance.

- The ``.whl`` file extension is matched case-insensitively.

Visit <https://github.com/wheelodex/wheel-filename> for more information.
"""

from __future__ import annotations
from collections.abc import Iterator
import os
import os.path
import re
from typing import NamedTuple, Optional

__version__ = "1.4.2"
__author__ = "John Thorvald Wodder II"
__author_email__ = "wheel-filename@varonathe.org"
__license__ = "MIT"
__url__ = "https://github.com/wheelodex/wheel-filename"

__all__ = [
    "InvalidFilenameError",
    "ParsedWheelFilename",
    "parse_wheel_filename",
]

# These patterns are interpreted with re.UNICODE in effect, so there's probably
# some character that matches \d but not \w that needs to be included
PYTHON_TAG_RGX = r"[\w\d]+"
ABI_TAG_RGX = r"[\w\d]+"
PLATFORM_TAG_RGX = r"[\w\d]+"

WHEEL_FILENAME_CRGX = re.compile(
    r"(?P<project>[A-Za-z0-9](?:[A-Za-z0-9._]*[A-Za-z0-9])?)"
    r"-(?P<version>[A-Za-z0-9_.!+]+)"
    r"(?:-(?P<build>[0-9][\w\d.]*))?"
    r"-(?P<python_tags>{0}(?:\.{0})*)"
    r"-(?P<abi_tags>{1}(?:\.{1})*)"
    r"-(?P<platform_tags>{2}(?:\.{2})*)"
    r"\.[Ww][Hh][Ll]".format(PYTHON_TAG_RGX, ABI_TAG_RGX, PLATFORM_TAG_RGX)
)


class ParsedWheelFilename(NamedTuple):
    project: str
    version: str
    build: Optional[str]
    python_tags: list[str]
    abi_tags: list[str]
    platform_tags: list[str]

    def __str__(self) -> str:
        if self.build:
            fmt = "{0.project}-{0.version}-{0.build}-{1}-{2}-{3}.whl"
        else:
            fmt = "{0.project}-{0.version}-{1}-{2}-{3}.whl"
        return fmt.format(
            self,
            ".".join(self.python_tags),
            ".".join(self.abi_tags),
            ".".join(self.platform_tags),
        )

    def tag_triples(self) -> Iterator[str]:
        """
        Returns a generator of all simple tag triples formed from the tags in
        the filename
        """
        for py in self.python_tags:
            for abi in self.abi_tags:
                for plat in self.platform_tags:
                    yield "-".join([py, abi, plat])


def parse_wheel_filename(
    filename: str | bytes | os.PathLike[str] | os.PathLike[bytes],
) -> ParsedWheelFilename:
    """
    Parse a wheel filename into its components

    :param path filename: a wheel path or filename
    :rtype: ParsedWheelFilename
    :raises InvalidFilenameError: if the filename is invalid
    """
    basename = os.path.basename(os.fsdecode(filename))
    m = WHEEL_FILENAME_CRGX.fullmatch(basename)
    if not m:
        raise InvalidFilenameError(basename)
    return ParsedWheelFilename(
        project=m.group("project"),
        version=m.group("version"),
        build=m.group("build"),
        python_tags=m.group("python_tags").split("."),
        abi_tags=m.group("abi_tags").split("."),
        platform_tags=m.group("platform_tags").split("."),
    )


class InvalidFilenameError(ValueError):
    """Raised when an invalid wheel filename is encountered"""

    filename: str

    def __init__(self, filename: str) -> None:
        #: The invalid filename
        self.filename = filename

    def __str__(self) -> str:
        return "Invalid wheel filename: " + repr(self.filename)

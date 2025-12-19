v2.0.0 (2025-12-19)
-------------------
- Support Python 3.14
- Drop support for Python 3.8 and 3.9
- Changed `ParsedWheelFilename` from a namedtuple to a dataclass
- **Breaking**: Renamed `ParsedWheelFilename` to `WheelFilename`
- **Breaking**: Renamed `parse_wheel_filename()` to `WheelFilename.parse()`
- **Breaking**: Renamed `InvalidFilenameError` to `ParseError`

v1.4.2 (2024-12-01)
-------------------
- Drop support for Python 3.6 and 3.7
- Support Python 3.11, 3.12, and 3.13
- Moved to wheelodex organization
- Migrated from setuptools to hatch

v1.4.1 (2022-05-31)
-------------------
- Refine return type annotation on `ParsedWheelFilename.tag_triples()`

v1.4.0 (2022-02-03)
-------------------
- Support Python 3.10
- Added a `wheel-filename` command that outputs wheel filename components as
  JSON

v1.3.0 (2021-03-18)
-------------------
- Support Python 3.9
- Paths passed to `parse_wheel_filename()` can now be `bytes` or
  `os.PathLike[bytes]`

v1.2.0 (2020-07-05)
-------------------
- Changed `ParsedWheelFilename` to a `namedtuple` so that it can be iterated
  over
- Dropped support for Python 3.5
- Added type annotations

v1.1.0 (2020-04-01)
-------------------
- `parse_wheel_filename()` now strips leading directory components from its
  argument before processing

v1.0.0 (2020-03-23)
-------------------
Split off code from [wheel-inspect](https://github.com/jwodder/wheel-inspect).

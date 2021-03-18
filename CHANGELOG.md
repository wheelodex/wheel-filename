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

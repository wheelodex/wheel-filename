from __future__ import annotations
import argparse
import json
import sys
from typing import Optional
from . import InvalidFilenameError, __version__, parse_wheel_filename


def main(argv: Optional[list[str]] = None) -> None:
    parser = argparse.ArgumentParser(description="Parse wheel filename")
    parser.add_argument(
        "-V", "--version", action="version", version=f"%(prog)s {__version__}"
    )
    parser.add_argument("filename")
    args = parser.parse_args(argv)
    try:
        pwf = parse_wheel_filename(args.filename)
    except InvalidFilenameError as e:
        sys.exit(f"wheel-filename: {e}")
    print(json.dumps(pwf._asdict(), indent=4))


if __name__ == "__main__":
    main()  # pragma: no cover

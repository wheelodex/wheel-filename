from __future__ import annotations
import argparse
from dataclasses import asdict
import json
import sys
from . import ParseError, WheelFilename, __version__


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Parse wheel filename")
    parser.add_argument(
        "-V", "--version", action="version", version=f"%(prog)s {__version__}"
    )
    parser.add_argument("filename")
    args = parser.parse_args(argv)
    try:
        pwf = WheelFilename.parse(args.filename)
    except ParseError as e:
        print(f"wheel-filename: {e}", file=sys.stderr)
        return 1
    print(json.dumps(asdict(pwf), indent=4))
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover

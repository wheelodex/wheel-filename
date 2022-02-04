import sys
import pytest
from wheel_filename.__main__ import main


def test_main(
    capsys: pytest.CaptureFixture[str], monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(
        sys, "argv", ["wheel-filename", "pip-18.0-py2.py3-none-any.whl"]
    )
    main()
    out, err = capsys.readouterr()
    assert out == (
        "{\n"
        '    "project": "pip",\n'
        '    "version": "18.0",\n'
        '    "build": null,\n'
        '    "python_tags": [\n'
        '        "py2",\n'
        '        "py3"\n'
        "    ],\n"
        '    "abi_tags": [\n'
        '        "none"\n'
        "    ],\n"
        '    "platform_tags": [\n'
        '        "any"\n'
        "    ]\n"
        "}\n"
    )
    assert err == ""


def test_main_error(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as excinfo:
        main(["dist/devtools-0.1-py35,py36-none-any.whl"])
    assert excinfo.value.args == (
        "wheel-filename: Invalid wheel filename: 'devtools-0.1-py35,py36-none-any.whl'",
    )
    out, err = capsys.readouterr()
    assert out == ""
    assert err == ""

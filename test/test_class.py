from wheel_filename import ParsedWheelFilename


def test_pwf_iterable() -> None:
    pwf = ParsedWheelFilename(
        project="project",
        version="1.2.3",
        build="1",
        python_tags=["py2", "py3"],
        abi_tags=["none"],
        platform_tags=["any"],
    )
    
    assert pwf.project == "project"
    assert pwf.version == "1.2.3"
    assert pwf.build == "1"
    assert pwf.python_tags == ["py2", "py3"]
    assert pwf.abi_tags == ["none"]
    assert pwf.platform_tags == ["any"]

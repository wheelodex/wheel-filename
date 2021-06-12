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
    project, version, build, pytags, abi_tags, platform_tags = pwf
    assert project == "project"
    assert version == "1.2.3"
    assert build == "1"
    assert pytags == ["py2", "py3"]
    assert abi_tags == ["none"]
    assert platform_tags == ["any"]

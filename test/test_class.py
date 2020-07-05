from unittest.mock  import sentinel
from wheel_filename import ParsedWheelFilename

def test_pwf_iterable():
    pwf = ParsedWheelFilename(
        project       = sentinel.PROJECT,
        version       = sentinel.VERSION,
        build         = sentinel.BUILD,
        python_tags   = sentinel.PYTAGS,
        abi_tags      = sentinel.ABI_TAGS,
        platform_tags = sentinel.PLATFORM_TAGS,
    )
    project, version, build, pytags, abi_tags, platform_tags = pwf
    assert project is sentinel.PROJECT
    assert version is sentinel.VERSION
    assert build is sentinel.BUILD
    assert pytags is sentinel.PYTAGS
    assert abi_tags is sentinel.ABI_TAGS
    assert platform_tags is sentinel.PLATFORM_TAGS

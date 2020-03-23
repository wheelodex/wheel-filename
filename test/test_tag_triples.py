import pytest
from   wheel_filename import ParsedWheelFilename

@pytest.mark.parametrize('parsed,triples', [
    (
        ParsedWheelFilename(
            project='cvxopt',
            version='1.2.0',
            build='001',
            python_tags=['cp34'],
            abi_tags=['cp34m'],
            platform_tags=[
                'macosx_10_6_intel',
                'macosx_10_9_intel',
                'macosx_10_9_x86_64',
                'macosx_10_10_intel',
                'macosx_10_10_x86_64',
            ],
        ),
        [
            'cp34-cp34m-macosx_10_6_intel',
            'cp34-cp34m-macosx_10_9_intel',
            'cp34-cp34m-macosx_10_9_x86_64',
            'cp34-cp34m-macosx_10_10_intel',
            'cp34-cp34m-macosx_10_10_x86_64',
        ],
    ),

    (
        ParsedWheelFilename(
            project='django_mbrowse',
            version='0.0.1',
            build='10',
            python_tags=['py2'],
            abi_tags=['none'],
            platform_tags=['any'],
        ),
        ['py2-none-any'],
    ),

    (
        ParsedWheelFilename(
            project='line.sep',
            version='0.2.0.dev1',
            build=None,
            python_tags=['py2', 'py3'],
            abi_tags=['none'],
            platform_tags=['any'],
        ),
        [
            'py2-none-any',
            'py3-none-any',
        ],
    ),

    (
        ParsedWheelFilename(
            project='PyQt3D',
            version='5.7.1',
            build='5.7.1',
            python_tags=['cp34', 'cp35', 'cp36'],
            abi_tags=['abi3'],
            platform_tags=['macosx_10_6_intel'],
        ),
        [
            'cp34-abi3-macosx_10_6_intel',
            'cp35-abi3-macosx_10_6_intel',
            'cp36-abi3-macosx_10_6_intel',
        ],
    ),
])
def test_tag_triples(parsed, triples):
    assert list(parsed.tag_triples()) == triples

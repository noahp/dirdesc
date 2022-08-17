import pytest

from dirdesc.dirdesc import load_dirdesc_yaml


@pytest.mark.parametrize(
    "yamldata,result",
    [
        (
            """
""",
            None,
        ),
        (
            """hello single string
""",
            "hello single string",
        ),
        (
            """---
somefile: somefile description
""",
            (None, {"somefile": "somefile description"}),
        ),
        (
            """hello single string
---
somefile: somefile description
""",
            ("hello single string", {"somefile": "somefile description"}),
        ),
    ],
)
def test_load_dirdesc_yaml(yamldata, result, tmp_path):
    """
    Check the yaml loader
    """
    testfile = tmp_path / "file.yaml"
    testfile.write_text(yamldata)
    desc = load_dirdesc_yaml(testfile)
    assert desc == result


@pytest.mark.parametrize(
    "yamldata",
    [
        """---
""",
        """key: val
---
""",
        """too
---
many
---
docs
""",
        """bad yaml
---
bad yaml
""",
    ],
)
def test_load_dirdesc_yaml_malformed(yamldata, tmp_path):
    """
    Check the yaml loader
    """
    testfile = tmp_path / "file.yaml"
    testfile.write_text(yamldata)
    with pytest.raises(AssertionError):
        desc = load_dirdesc_yaml(testfile)

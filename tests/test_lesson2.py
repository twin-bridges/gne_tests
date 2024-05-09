import pytest
from utilities import subprocess_runner, file_dir_exists

GIT = "/usr/bin/git"


def test_exercise3():
    """Test that git is installed and retrieve its version."""
    cmd_list = [GIT, "log", "--oneline"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, ".")

    assert return_code == 0
    assert std_err == ""
    assert "d9ae421 Initial commit of per-lesson directories" in std_out


@pytest.mark.parametrize(
    "directory, filename",
    [
        ("../lesson2", "simple.py"),
    ],
)
def test_exercise4(directory, filename):
    file_dir_exists(directory, filename)

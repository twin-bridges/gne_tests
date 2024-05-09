import pytest

from utilities import subprocess_runner, file_dir_exists, git_checkout
from TEST_CONSTANTS import GIT, REPOSITORY, DEFAULT_BRANCH


def test_exercise3():
    """Test that git is installed and retrieve its version."""
    cmd_list = [GIT, "log", "--oneline"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, REPOSITORY)

    assert return_code == 0
    assert std_err == ""
    assert "d9ae421 Initial commit of per-lesson directories" in std_out


@pytest.mark.parametrize(
    "directory, filename",
    [
        ("lesson2", "simple.py"),
    ],
)
def test_exercise4a(directory, filename):
    directory = REPOSITORY / directory
    file_dir_exists(directory, filename)


def test_exercise4b():
    commit = "d96bda4"
    git_checkout(commit)

    cmd_list = ["python3", "simple.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, REPOSITORY / "lesson2")

    assert return_code == 0
    assert std_err == ""
    assert "Hello world" in std_out

    git_checkout(DEFAULT_BRANCH)

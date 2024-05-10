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

    cmd_list = [GIT, "log", "--oneline"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, REPOSITORY / "lesson2")
    git_log = std_out.strip()
    assert return_code == 0
    assert std_err == ""
    assert len(git_log.splitlines()) == 2

    git_checkout(DEFAULT_BRANCH)


def test_exercise5():
    commit = "bf05110"
    git_checkout(commit)

    cmd_list = ["python3", "simple.py"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, REPOSITORY / "lesson2")

    assert return_code == 0
    assert std_err == ""
    assert "Hello world" in std_out
    assert "0" in std_out
    assert "99" in std_out

    cmd_list = [GIT, "log", "--oneline"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, REPOSITORY / "lesson2")
    git_log = std_out.strip()
    assert return_code == 0
    assert std_err == ""
    assert len(git_log.splitlines()) == 3

    git_checkout(DEFAULT_BRANCH)


def test_exercise6():
    commit = "bf05110"
    git_checkout(commit)

    directory = REPOSITORY / "lesson2"
    file_dir_exists(directory, "not-empty")

    commit = "4b46a05"
    git_checkout(commit)

    # File should NOT exist here
    file_dir_exists(directory, "not-empty", invert=True)

    cmd_list = [GIT, "log", "--oneline"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, REPOSITORY / "lesson2")
    git_log = std_out.strip()
    assert return_code == 0
    assert std_err == ""
    assert len(git_log.splitlines()) == 4

    for commit in ["4b46a05", "bf05110", "d96bda4", "d9ae421"]:
        assert commit in std_out, f"Commit not found: {commit}"

    git_checkout(DEFAULT_BRANCH)


def test_exercise7():
    hash_val = "4b46a054b616b06fdf5b5f797e76a522fed4764e"
    cmd_list = [GIT, "cat-file", "-p", hash_val]
    std_out, std_err, return_code = subprocess_runner(cmd_list, REPOSITORY / "lesson2")

    assert return_code == 0
    assert std_err == ""

    assert "tree acf88e6" in std_out
    assert "parent bf05110" in std_out
    assert "author Kirk Byers <ktbyers@twb-tech.com>" in std_out
    assert "committer Kirk Byers <ktbyers@twb-tech.com>" in std_out

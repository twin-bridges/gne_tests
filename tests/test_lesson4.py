import os
from pathlib import Path
import re

from utilities import (
    subprocess_runner,
    file_dir_exists,
)
from TEST_CONSTANTS import GIT, L4_REPOSITORY


def test_exercise1():
    """Test that git is installed and retrieve its version."""

    test_dir = Path.cwd()

    home = Path.home()
    os.chdir(home)

    directory = home / "remotes_gne_exercises"
    if directory.exists() and directory.is_dir():
        assert False

    url = "https://github.com/twin-bridges/gne_exercises"
    repo_dir = "remotes_gne_exercises"
    cmd_list = [GIT, "clone", url, repo_dir]
    std_out, _, return_code = subprocess_runner(cmd_list, home)

    assert return_code == 0
    if directory.exists() and directory.is_dir():
        assert True

    os.chdir(test_dir)


def test_exercise1b():
    cmd_list = [GIT, "remote", "-v"]
    std_out, _, _ = subprocess_runner(cmd_list, L4_REPOSITORY, check_errors=True)

    assert "origin" in std_out
    assert "https://github.com/twin-bridges/gne_exercises" in std_out
    assert "fetch" in std_out
    assert "push" in std_out


def test_exercise1c():
    url = "https://github.com/twin-bridges/gne_exercises"
    cmd_list = [GIT, "remote", "add", "my_remote", url]
    std_out, _, _ = subprocess_runner(cmd_list, L4_REPOSITORY, check_errors=True)

    cmd_list = [GIT, "remote", "-v"]
    std_out, _, _ = subprocess_runner(cmd_list, L4_REPOSITORY, check_errors=True)
    assert re.search(rf"my_remote.*{url}.*fetch", std_out)
    assert re.search(rf"my_remote.*{url}.*push", std_out)


def test_exercise1d():
    cmd_list = [GIT, "fetch", "my_remote"]
    std_out, std_err, return_code = subprocess_runner(
        cmd_list, L4_REPOSITORY, check_errors=False
    )

    assert return_code == 0
    assert "From https://github.com/twin-bridges/gne_exercises" in std_err
    assert re.search(r"new branch.*main.*my_remote/main", std_err)
    assert re.search(r"new branch.*l4\-testing.*my_remote/l4\-testing", std_err)

    cmd_list = [GIT, "branch", "-r"]
    std_out, _, _ = subprocess_runner(cmd_list, L4_REPOSITORY, check_errors=True)
    assert "my_remote/l4-testing" in std_out
    assert "my_remote/main" in std_out
    assert "origin/l4-testing" in std_out
    assert "origin/main" in std_out
    assert re.search(r"origin/HEAD.*origin/main", std_out)


def test_exercise2():
    cmd_list = [GIT, "checkout", "-b", "l4-testing", "origin/l4-testing"]
    std_out, std_err, return_code = subprocess_runner(
        cmd_list, L4_REPOSITORY, check_errors=False
    )
    assert return_code == 0
    assert re.search(r"Switched to a new branch.*l4-testing", std_err)

    cmd_list = [GIT, "branch"]
    std_out, _, _ = subprocess_runner(cmd_list, L4_REPOSITORY, check_errors=True)
    assert re.search(r"\*.l4\-testing", std_out)

    home = Path.home()
    directory = home / "remotes_gne_exercises" / "lesson4"
    filename = "WELCOME.md"
    file_dir_exists(directory, filename, invert=False)

    cmd_list = [GIT, "log", "--oneline"]
    std_out, _, _ = subprocess_runner(cmd_list, L4_REPOSITORY, check_errors=True)
    git_log_line1 = std_out.splitlines()[0]
    assert "89c7b24 Add the WELCOME.md file for Lesson4" in git_log_line1

    cmd_list = [GIT, "branch", "-vv"]
    std_out, _, _ = subprocess_runner(cmd_list, L4_REPOSITORY, check_errors=True)
    assert re.search(r"\*.l4\-testing.*89c7b24.\[origin.l4\-testing\]", std_out)
    assert re.search(r"\s*main.*\[origin.main\]", std_out)

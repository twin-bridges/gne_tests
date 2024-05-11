import os
from pathlib import Path
import re

from utilities import (
    subprocess_runner,
    git_checkout,
    file_dir_exists,
    subprocess_runner_stdin,
)
from TEST_CONSTANTS import GIT, L4_REPOSITORY, DEFAULT_BRANCH

# FIX: fixture remove remotes_gne_exercises after
# FIX: remotes_gne_exercises doesn't exist at the beginning
# FIX: very beginning of exercise4 in Drip


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


"""

2a. You should be able create a branch named 'l4-testing' that is based upon my 'origin/l4-testing' branch by executing the following command:
git checkout -b l4-testing origin/l4-testing

2b. Look at your current branch and make sure it is using l4-testing.

2c. Look at your current working directory and 'git log' it should be different than what you previously had (on your 'gne_exercises' repository). You should have a file name "WELCOME.md" in the "lesson4" directory.

2d. Execute "git branch -vv" to see the tracking branches. You should have a tracking branch both for the 'main' branch and for the 'l4-testing' branch.


We will do additional 'git pull' and 'git push' work once we get your GitHub repository setup in the next lesson.



"""

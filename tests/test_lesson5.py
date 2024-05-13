import re

from utilities import subprocess_runner, git_checkout
from TEST_CONSTANTS import GIT, REPOSITORY


def test_exercise2():
    # Check if 'my_remote' already exists and remove it
    cmd_list = [GIT, "remote", "-v"]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)
    if re.search(r"my_remote\s*\S*jupiter\-calisto", std_out):
        cmd_list = [GIT, "remote", "remove", "my_remote"]
        std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)

    url = "https://github.com/jupiter-calisto/gne_exercises"
    cmd_list = [GIT, "remote", "add", "my_remote", url]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)


def test_exercise5():
    branch = "l5-feature1"
    cmd_list = [GIT, "branch", branch]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)
    git_checkout(branch)
    git_checkout("main")


def test_exercise6():
    branch = "l5-feature1"

    cmd_list = [GIT, "log", "--oneline"]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)
    assert re.search(
        r"502db9d Merge pull request #1 from twin\-bridges.l5\-feature1", std_out
    )
    assert re.search(r"aba7db0 Add broadcast address", std_out)

    cmd_list = [GIT, "branch", "-d", branch]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)

import re

from utilities import subprocess_runner, git_checkout
from TEST_CONSTANTS import GIT, REPOSITORY


def commit_change(file_name):
    cmd_list = [GIT, "add", file_name]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)

    cmd_list = [GIT, "commit", "-m", "TESTS: Lesson6, Ex3"]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)
    assert "TESTS: Lesson6, Ex3" in std_out
    assert "1 file changed, 0 insertions(+), 0 deletions(-)" in std_out
    assert "create mode 100644 test_lesson6_ex3.txt" in std_out

    # Clean 'git status'
    cmd_list = [GIT, "status"]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)
    assert "nothing to commit, working tree clean" in std_out


def test_exercise1a():

    commit = "983a8b7"
    git_checkout(commit)

    cmd_list = [GIT, "log", "--oneline"]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)
    git_log_line1 = std_out.splitlines()[0]
    assert re.search(r"983a8b7 Tag exercise", std_out)

    git_checkout(tag="v0.1")

    cmd_list = [GIT, "log", "--oneline"]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)
    git_log_line1 = std_out.splitlines()[0]
    assert re.search(r"983a8b7 Tag exercise", git_log_line1)

    git_checkout(branch="main")


def test_exercise1b():

    cmd_list = [GIT, "tag", "--list"]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)
    assert "v0.1" in std_out


def test_exercise2a():

    cmd_list = [GIT, "config", "--global", "init.defaultBranch", "test123"]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)

    cmd_list = [GIT, "config", "init.defaultBranch"]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)
    assert "test123" in std_out

    cmd_list = [GIT, "config", "--global", "init.defaultBranch", "main"]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)

    cmd_list = [GIT, "config", "init.defaultBranch"]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)
    assert "main" in std_out


def test_exercise2b():

    cmd_list = [GIT, "config", "--list"]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)
    assert "init.defaultbranch=main" in std_out
    assert "core.bare=false" in std_out


def test_exercise2c():

    cmd_list = [GIT, "config", "pull.rebase", "false"]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)

    cmd_list = [GIT, "config", "--list"]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)
    assert "pull.rebase=false" in std_out


def test_exercise2d():

    cmd_list = [GIT, "config", "--list", "--global"]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)
    assert "init.defaultbranch=main" in std_out

    cmd_list = [GIT, "config", "--list", "--local"]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)
    assert "pull.rebase=false" in std_out


def test_exercise3():

    # Ex 3a
    cmd_list = [GIT, "log", "--oneline"]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)
    first_line = std_out.splitlines()[0]
    original_commit = first_line.split()[0]

    file_name = "test_lesson6_ex3.txt"
    cmd_list = ["touch", file_name]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)

    commit_change(file_name)

    # Ex 3b
    cmd_list = [GIT, "reset", "--soft", "HEAD~1"]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)

    # Soft reset should restore the change to staging
    cmd_list = [GIT, "status"]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)
    pattern = re.escape(r"new file:   test_lesson6_ex3.txt")
    assert re.search(pattern, std_out)

    # Ex 3c
    commit_change(file_name)

    # Ex 3d
    cmd_list = [GIT, "reset", "--mixed", "HEAD~1"]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)

    # Mixed reset should undo the commit and revert staging (unstage the file)
    cmd_list = [GIT, "status"]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)
    assert "Untracked files:" in std_out
    assert """use "git add <file>..." to include""" in std_out
    assert "test_lesson6_ex3.txt" in std_out

    # Ex 3e
    commit_change(file_name)

    # Ex 3f
    cmd_list = [GIT, "reset", "--hard", "HEAD~1"]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)
    assert f"HEAD is now at {original_commit}" in std_out

    cmd_list = [GIT, "status"]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)
    assert "nothing to commit, working tree clean" in std_out

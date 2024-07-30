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
    # Ex 1a
    cmd_list = [GIT, "config", "pull.rebase"]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)
    assert "false" in std_out

    commit = "b613a36"
    cmd_list = [GIT, "log", "--oneline", commit]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)

    commit_msg = std_out.splitlines()[0]
    assert "Adding 'show_run.py program" in commit_msg

    commit = "a021525"
    cmd_list = [GIT, "log", "--oneline", commit]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)
    commit_msg = std_out.splitlines()[0]

    assert "Adding a comment to 'show_run.py' program" in commit_msg


def test_exercise1b():
    commit = "a50bc2b"
    cmd_list = [GIT, "log", "--oneline", commit]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)

    commit_msg = std_out.splitlines()[0]
    assert "Adding 'proxy.py' SSH connection program" in commit_msg


def test_exercise1c():
    cmd_list = [GIT, "config", "merge.ff"]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)
    assert "false" in std_out


def test_exercise1e():
    commit = "65b04d3"
    cmd_list = [GIT, "log", "--oneline", commit]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)

    commit0, commit1, commit2, commit3 = std_out.splitlines()[:4]
    assert "65b04d3 Merge branch 'feature/proxy'" in commit0
    assert "a50bc2b Adding 'proxy.py' SSH connection program" in commit1
    assert "b1b6939 Lesson6, exercise3 reference solution" in commit2
    assert "1f62d32 Lesson6, ex3" in commit3


def test_exercise2b():
    commit = "fc21498"
    cmd_list = [GIT, "log", "--oneline", commit]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)
    commit0, commit1, commit2, commit3 = std_out.splitlines()[:4]

    assert "Adding a comment to 'show_run.py' program" in commit0
    assert "208cf63 Adding 'show_run.py program" in commit1


def test_exercise2d():
    commit = "351963c"
    cmd_list = [GIT, "log", "--oneline", commit]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)
    commit0, commit1, commit2, commit3 = std_out.splitlines()[:4]

    assert "Merge branch 'feature/show-run'" in commit0
    assert "Adding a comment to 'show_run.py' program" in commit1


def test_exercise3b():
    commit = "b1b6939"
    cmd_list = [GIT, "log", "--oneline", commit]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)
    commit0 = std_out.splitlines()[0]

    assert "Lesson6, exercise3 reference solution" in commit0

    branch = "feature/proxy"
    git_checkout(branch=branch)

    cmd_list = [GIT, "log", "--oneline"]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)
    commit0 = std_out.splitlines()[0]
    assert "Adding 'proxy.py' SSH connection program" in commit0

    branch = "feature/show-run"
    git_checkout(branch=branch)

    cmd_list = [GIT, "log", "--oneline"]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)
    commit0 = std_out.splitlines()[0]
    assert "Adding a comment to 'show_run.py' program" in commit0

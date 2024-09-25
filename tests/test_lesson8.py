from utilities import subprocess_runner, git_checkout, file_dir_exists
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


def test_exercise1a(directory="lesson8", filename="amend.txt"):
    """Test that a given file exists in a specified directory."""
    directory = REPOSITORY / directory
    file_dir_exists(directory, filename)

    commit = "4892d4a"
    cmd_list = [GIT, "log", "--oneline", commit]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)

    commit_msg = std_out.splitlines()[0]
    # Don't exactly have the original history given that I am amending commits.
    assert "Testing commit amend (modified again)" in commit_msg
    # assert "Testing commit amend" in commit_msg


def test_exercise1b():
    commit = "4892d4a"
    cmd_list = [GIT, "log", "--oneline", commit]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)
    commit_msg = std_out.splitlines()[0]

    # assert "Testing commit amend" in commit_msg
    # Don't exactly have the original history given that I am amending commits.
    assert "Testing commit amend (modified again)" in commit_msg
    # assert "Testing commit amend (modified)" in commit_msg


def test_exercise1c():
    commit = "4892d4a"
    cmd_list = [GIT, "log", "--oneline", commit]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)
    commit_msg = std_out.splitlines()[0]

    assert "Testing commit amend (modified again)" in commit_msg


def test_exercise2a():
    commit = "45c93e9"
    cmd_list = [GIT, "log", "--oneline", commit]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)

    commit3, commit1_2 = std_out.splitlines()[:2]
    # Don't exactly have the original history given that I am rebasing interactive.
    assert "rebase interactive commit3 (amended test_file.py)" in commit3
    assert "rebase interactive commit1 & commit2 (modified)" in commit1_2
    # assert "rebase interactive commit3" in commit3
    # assert "rebase interactive commit2" in commit2
    # assert "rebase interactive commit1" in commit1


def test_exercise2b():
    commit = "45c93e9"
    cmd_list = [GIT, "log", "--oneline", commit]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)

    commit3, commit1_2 = std_out.splitlines()[:2]
    # Don't exactly have the original history given that I am rebasing interactive.
    assert "rebase interactive commit3 (amended test_file.py)" in commit3
    assert "rebase interactive commit1 & commit2 (modified)" in commit1_2
    # assert "rebase interactive commit3" in commit3
    # assert "rebase interactive commit2 (modified)" in commit2
    # assert "rebase interactive commit1" in commit1


def test_exercise2c(directory="lesson8", filename="test_file.py"):
    commit = "45c93e9"
    cmd_list = [GIT, "log", "--oneline", commit]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)

    commit3, commit1_2 = std_out.splitlines()[:2]
    # Don't exactly have the original history given that I am rebasing interactive.
    assert "rebase interactive commit3 (amended test_file.py)" in commit3
    assert "rebase interactive commit1 & commit2 (modified)" in commit1_2
    # assert "rebase interactive commit3 (amended test_file.py)" in commit3
    # assert "rebase interactive commit2 (modified)" in commit2
    # assert "rebase interactive commit1" in commit1

    directory = REPOSITORY / directory
    file_dir_exists(directory, filename)


def test_exercise2d():
    commit = "45c93e9"
    cmd_list = [GIT, "log", "--oneline", commit]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)

    commit3, commit2_1 = std_out.splitlines()[:2]
    assert "rebase interactive commit3 (amended test_file.py)" in commit3
    assert "rebase interactive commit1 & commit2 (modified)" in commit2_1


def test_exercise2e():
    commit = "45c93e9"
    cmd_list = [GIT, "log", "--oneline", commit]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)

    # Don't exactly have the original history given that I am rebasing interactive.
    commit3, commit2_1 = std_out.splitlines()[:2]
    # assert "rebase interactive commit4" in commit4
    assert "rebase interactive commit3 (amended test_file.py)" in commit3
    assert "rebase interactive commit1 & commit2 (modified)" in commit2_1

    commit = "205affc"
    cmd_list = [GIT, "log", "--oneline", commit]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)

    commitx, commit3, commit2_1 = std_out.splitlines()[:3]
    assert "Testing git reflog1" in commitx
    assert "rebase interactive commit3 (amended test_file.py)" in commit3
    assert "rebase interactive commit1 & commit2 (modified)" in commit2_1


def test_exercise3a(directory="lesson8", filename="reflog.txt"):
    """Test that a given file exists in a specified directory."""
    directory = REPOSITORY / directory
    file_dir_exists(directory, filename)

    commit = "e5bd02b"
    cmd_list = [GIT, "log", "--oneline", commit]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)

    commit_rl2, commit_rl1, commit3, commit2_1 = std_out.splitlines()[:4]
    assert "Testing git reflog2" in commit_rl2
    assert "Testing git reflog1" in commit_rl1
    assert "rebase interactive commit3 (amended test_file.py)" in commit3
    assert "rebase interactive commit1 & commit2 (modified)" in commit2_1


def test_exercise3c():
    commit = "45c93e9"
    cmd_list = [GIT, "log", "--oneline", commit]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)

    # Don't have the lost commit any longer (so fudge a bit in testing)
    commit3, commit2_1 = std_out.splitlines()[:2]
    # assert "7636b66 rebase interactive commit4" in commit4
    assert "rebase interactive commit3 (amended test_file.py)" in commit3
    assert "rebase interactive commit1 & commit2 (modified)" in commit2_1

    branch = "main"
    git_checkout(branch=branch)

from utilities import (
    subprocess_runner,
    git_checkout,
    file_dir_exists,
    subprocess_runner_stdin,
)
from TEST_CONSTANTS import GIT, REPOSITORY, DEFAULT_BRANCH


def test_exercise1():
    """Test that git is installed and retrieve its version."""
    cmd_list = [GIT, "log", "--oneline"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, REPOSITORY)

    assert return_code == 0
    assert std_err == ""
    assert "125d703 l3-feature1: commit1" in std_out
    assert "6c79bba l3-feature1: commit2" in std_out


def test_exercise1f():
    cmd_list = [GIT, "branch"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, REPOSITORY)

    assert return_code == 0
    assert std_err == ""
    assert "l3-feature1" not in std_out


def test_exercise2():
    cmd_list = [GIT, "log", "--oneline"]
    std_out, std_err, return_code = subprocess_runner(
        cmd_list, REPOSITORY, check_errors=True
    )

    assert "97e6514 l3-feature2: commit1" in std_out
    assert "fc3ea62 l3-feature2: commit2" in std_out


def test_exercise2f():
    cmd_list = [GIT, "branch"]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)

    assert "l3-feature2" not in std_out


def test_exercise3():
    commit = "8eec4c5"
    git_checkout(commit)

    directory = REPOSITORY / "lesson3"
    file_dir_exists(directory, "my_script.py")

    cmd_list = ["python3", "my_script.py"]
    std_out, _, _ = subprocess_runner(cmd_list, directory, check_errors=True)

    assert "192" in std_out
    assert "168" in std_out

    commit = "19b1e77"
    git_checkout(commit)
    # Re-run my_script.py
    std_out, _, _ = subprocess_runner(cmd_list, directory, check_errors=True)

    assert "192" not in std_out
    assert "168" not in std_out
    assert "10" in std_out

    commit = "f7bd57e"
    git_checkout(commit)

    # Re-run my_script.py
    stdin_response = "10.88.107.100\n"
    std_out, _, _ = subprocess_runner_stdin(
        cmd_list, stdin_response, directory, check_errors=True
    )

    assert "192" not in std_out
    assert "168" not in std_out
    assert "107" in std_out

    # Re-run my_script.py
    stdin_response = "\n"
    std_out, _, _ = subprocess_runner_stdin(
        cmd_list, stdin_response, directory, check_errors=True
    )

    assert "192" not in std_out
    assert "168" not in std_out
    assert "10" in std_out

    git_checkout(DEFAULT_BRANCH)


def test_exercise3i():
    cmd_list = [GIT, "branch"]
    std_out, _, _ = subprocess_runner(cmd_list, REPOSITORY, check_errors=True)

    assert "l3-feature3" not in std_out

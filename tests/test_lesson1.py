import pytest
from utilities import subprocess_runner, file_dir_exists

GIT = "/usr/bin/git"


def test_git_version():
    """Test that git is installed and retrieve its version."""
    cmd_list = [GIT, "--version"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, ".")
    git_version = std_out

    assert return_code == 0
    assert std_err == ""
    assert git_version is not None
    assert "git version" in git_version

    # Example check for a specific version or version range
    # Adjust this according to your version requirements
    version_number = git_version.split()[-1]
    major_version, minor_version, _ = version_number.split(".")
    assert int(major_version) >= 2
    assert int(minor_version) >= 40


@pytest.mark.parametrize(
    "directory, filename",
    [
        ("../lesson1", "not-empty"),
        ("../lesson2", "simple.py"),
        ("../lesson3", "not-empty"),
        ("../lesson4", "not-empty"),
        ("../lesson5", "not-empty"),
        ("../lesson6", "not-empty"),
        ("../lesson7", "not-empty"),
    ],
)
def test_lesson_dirs_exists(directory, filename):
    """Test that a given file exists in a specified directory."""
    file_dir_exists(directory, filename)


@pytest.mark.parametrize("branch_name", ["main"])
def test_branch_exists(branch_name):
    """Test that the specified branch exists in the local Git repository."""

    cmd_list = [GIT, "branch", "--list"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, ".")

    assert return_code == 0
    assert std_err == ""
    git_branch_list = std_out

    err_msg = f"Branch '{branch_name}' does not exist in the local repository."
    assert branch_name in git_branch_list, err_msg


def test_repository_is_gne_exercises():
    """Test that the Git repository name matches the expected name."""

    expected_repo = "gne_exercises"

    cmd_list = [GIT, "remote", "get-url", "origin"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, ".")

    assert return_code == 0
    assert std_err == ""

    remote_url = std_out.strip()

    # Extract the repository name from the URL
    if remote_url.endswith(".git"):
        remote_url = remote_url[:-4]
    repo_name = remote_url.split("/")[-1]

    err_msg = f"Expected repository name '{expected_repo}', but received '{repo_name}'."
    assert repo_name == expected_repo, err_msg


def test_git_user():
    """Test that the Git repository name matches the expected name."""

    f_name = "Jerome"
    l_name = "Morrow"
    set_user = [GIT, "config", "--global", "user.name", f"{f_name} {l_name}"]

    # Set the user (as per the lesson instructions)
    std_out, std_err, return_code = subprocess_runner(set_user, ".")
    assert return_code == 0
    assert std_err == ""

    cmd_list = [GIT, "config", "user.name"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, ".")
    assert return_code == 0
    assert std_err == ""
    assert f_name in std_out
    assert l_name in std_out


def test_git_email():
    """Test that the Git repository name matches the expected name."""

    email = "j.morrow@rockets.org"
    set_email = [GIT, "config", "--global", "user.email", email]

    # Set the user (as per the lesson instructions)
    std_out, std_err, return_code = subprocess_runner(set_email, ".")
    assert return_code == 0
    assert std_err == ""

    cmd_list = [GIT, "config", "user.email"]
    std_out, std_err, return_code = subprocess_runner(cmd_list, ".")
    assert return_code == 0
    assert std_err == ""
    assert email in std_out

import subprocess
from pathlib import Path

from TEST_CONSTANTS import GIT, REPOSITORY



def subprocess_runner(cmd_list, exercise_dir):
    with subprocess.Popen(
        cmd_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=exercise_dir
    ) as proc:
        std_out, std_err = proc.communicate()
    return (std_out.decode(), std_err.decode(), proc.returncode)


def file_dir_exists(directory, filename):
    """Test that a given file exists in a specified directory."""
    file_path = Path(directory) / filename
    err_msg = f"Expected file '{filename}' to be in directory '{directory}', but it was not found."
    assert file_path.is_file(), err_msg


def git_checkout(commit=None, branch=None):
    """Checkout a specific Git commit"""
    if commit:
        cmd_list = [GIT, "checkout", commit]
    elif branch:
        cmd_list = [GIT, "checkout", branch]
    std_out, std_err, return_code = subprocess_runner(cmd_list, REPOSITORY)
    if return_code != 0:
        # Checkout in detatched head will have output on std_err normally.
        # so use return_code to see if the command ran properly.
        msg = f"Failed to checkout commit/branch ({cmd_list}):\n\n{std_err}"
        raise RuntimeError(msg)

    return

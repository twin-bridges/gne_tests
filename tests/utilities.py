import subprocess
from pathlib import Path

from TEST_CONSTANTS import GIT, REPOSITORY


def subprocess_runner(cmd_list, exercise_dir, check_errors=False):
    with subprocess.Popen(
        cmd_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=exercise_dir
    ) as proc:
        std_out, std_err = proc.communicate()
    std_out, std_err, return_code = (
        std_out.decode(),
        std_err.decode(),
        proc.returncode,
    )
    if check_errors:
        assert std_err == ""
        assert return_code == 0
    return (std_out, std_err, return_code)


def subprocess_runner_stdin(cmd_list, stdin_response, exercise_dir, check_errors=False):
    with subprocess.Popen(
        cmd_list,
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE,
        stderr=subprocess.PIPE,
        # Use line-buffering (send line when a newline is encountered)
        bufsize=1,
        # Input/output gets converted to/from text
        universal_newlines=True,
        cwd=exercise_dir,
    ) as proc:
        std_out, std_err = proc.communicate(input=stdin_response)

    return_code = proc.returncode
    if check_errors:
        assert std_err == ""
        assert return_code == 0
    return (std_out, std_err, return_code)


def file_dir_exists(directory, filename, invert=False):
    """Test that a given file exists in a specified directory."""
    file_path = Path(directory) / filename
    if invert:
        # File does not exist
        err_msg = (
            f"Expected file '{directory}/{filename}' to not exist, but it was found?"
        )
        assert not file_path.is_file(), err_msg
    else:
        # File exists
        err_msg = (
            f"Expected file '{directory}/{filename}' to exist, but it was not found."
        )
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

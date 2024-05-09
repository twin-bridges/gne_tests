import subprocess
from pathlib import Path


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

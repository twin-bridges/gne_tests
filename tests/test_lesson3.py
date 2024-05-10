from utilities import subprocess_runner, git_checkout, file_dir_exists
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
    std_out, std_err, return_code = subprocess_runner(
        cmd_list, directory, check_errors=True
    )

    assert "192" not in std_out
    assert "168" not in std_out
    assert "10" in std_out

    git_checkout(DEFAULT_BRANCH)


"""


3c. Create and checkout a branch named "l3-feature3". Modify "my_script.py" by changing the ip_addr variable as follows:
ip_addr = "10.1.1.1"
for octet in ip_addr.split("."):
    print(octet)

3d. Commit this change into the "l3-feature3" branch with a commit message of "Changing IP address in my_script.py".

3e. Switch back to the main branch and edit the "my_script.py file" to be:
ip_addr = input("Enter IP address: ")
for octet in ip_addr.split("."):
    print(octet)

3f. Commit this change into "main" with a commit message of "Prompt user for IP address in my_script.py"

3g. Merge "l3-feature3" into "main". You will have a merge conflict at this point.

Resolve the merge conflict such that your end code looks as follows:
ip_addr = input("Enter IP address: ")
if not ip_addr:
    ip_addr = "10.1.1.1"
for octet in ip_addr.split("."):
    print(octet)

You will need to 'git add' and 'git commit' my_script.py after you resolve the merge conflict by editing the file.

3h. Review your Git Log by using:
git log --oneline --graph --decorate

From this command, you should be able to observe that your last commit (that resolved the merge conflict) has two parents. One parent is the last commit from 'main'; the other parent is the commit on the 'l3-feature3' branch.

3i. Delete the "l3-feature3" branch (the changes have now been merged into 'main').

"""

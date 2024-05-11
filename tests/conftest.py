import pytest
from pathlib import Path
import shutil
from datetime import datetime


def mv_remotes_gne_exercises(src, dst):
    shutil.move(str(src), str(dst))


@pytest.fixture(scope="session", autouse=True)
def backup_and_restore_gitconfig():
    # BEFORE TESTS ####
    home = Path.home()
    gitconfig = home / ".gitconfig"

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup_gitconfig = home / f".gitconfig.backup.{timestamp}"

    # Create a backup of the original gitconfig if it exists
    if gitconfig.exists():
        shutil.copy(gitconfig, backup_gitconfig)

    # Make sure 'remotes_gne_exercises' dir doesn't exist
    directory = home / "remotes_gne_exercises"
    dest_dir = home / "junk1" / f"remotes_gne_exercises.{timestamp}"
    if directory.exists() and directory.is_dir():
        mv_remotes_gne_exercises(src=directory, dst=dest_dir)

    # TESTS RUN ####
    yield

    # AFTER TESTS ####
    if backup_gitconfig.exists():
        shutil.copy(backup_gitconfig, gitconfig)
        print(f"\n\nRestored from {backup_gitconfig} to {gitconfig}\n")
        # backup_gitconfig.unlink()
    else:
        print(f"\n\nNo backup gitconfig found at {backup_gitconfig}\n")

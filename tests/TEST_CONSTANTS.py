from pathlib import Path
import os

HOME = Path.home()
GIT = "/usr/bin/git"
DEFAULT_BRANCH = "main"
REPOSITORY = HOME / "gne_exercises"
L4_REPOSITORY = HOME / "remotes_gne_exercises"

if os.getenv("GITHUB_ACTIONS"):
    # GH-Actions uses '/home/runner/work/gne_tests/gne_tests'
    # with the very final dir being the repo.
    HOME = HOME / "work" / "gne_tests"
    REPOSITORY = HOME / "gne_exercises"
    L4_REPOSITORY = HOME / "remotes_gne_exercises"

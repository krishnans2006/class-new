import os
import subprocess
import time
import webbrowser

REPO_URL = "https://github.com/new?template_name=class-template&template_owner=krishnans2006&owner=krishnans2006&name=class-{name}&visibility=private"
PAT_URL = "https://github.com/krishnans2006/class-{name}/settings/secrets/actions/new"
CLONE_URL = "git@github.com:krishnans2006/class-{name}"

file_path = os.path.realpath(__file__)

# Set dir to the hub directory
dir = os.path.dirname(file_path)
dir_parent = os.path.dirname(dir)
while dir_parent != dir:
    if os.path.exists(os.path.join(dir, ".gitmodules")):
        break
    dir, dir_parent = dir_parent, os.path.dirname(dir_parent)
else:
    raise RuntimeError("Could not find hub directory")

os.chdir(dir)

repo_name = input("Enter the name of the repository: ")

print("\nCreate the repository...")
webbrowser.open(REPO_URL.format(name=repo_name))
time.sleep(5)
input("Press enter when done...")

print("\nAdd a secret with the name 'UPDATE_SUBMODULE_PAT'...")
webbrowser.open(PAT_URL.format(name=repo_name))
input("Press enter when done...")

clone_path = input("\nEnter the path to clone the repository to, relative to the root of the repository: ")
subprocess.run(["git", "submodule", "add", CLONE_URL.format(name=repo_name), clone_path])
subprocess.run(["git", "add", ".gitmodules", clone_path])
subprocess.run(["git", "commit", "-m", f"Add {repo_name} class"])
subprocess.run(["git", "push"])

print("\nDone!")

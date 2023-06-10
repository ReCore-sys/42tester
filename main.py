import json
import os
import re
import sys
from glob import glob
from pathlib import Path

from rich import print as cprint


def find_sub_dirs(path, depth=2):
    path = Path(path)
    assert path.exists(), f'Path: {path} does not exist'
    depth_search = '*/' * depth
    search_pattern = os.path.join(path, depth_search)
    return list(glob(f'{search_pattern}'))


projectconfigs = [{},{}]
cprint("[green]Starting...[/green]")
exercise = {}
# Load the json files
with open("./projects.json", "r") as f:
    projectconfigs = json.load(f)
with open("./config.json", "r") as f:
    exercise = json.load(f)
# Validate the profiles
if (len(projectconfigs) > 0):
    cprint(f"[green]{len(projectconfigs)} profiles found[/green]")
else:
    cprint("[red]No testing profiles found[/red]")

# Get and validate the name of the project we wanna test
if len(sys.argv) < 2:
    cprint("[red]No project provided. Please run the program again and supply a project[/red]")
    exit()
projnames = [a for a in projectconfigs]
if sys.argv[1].lower() not in projnames:
    cprint("[red]Invalid project name. Please run the program again and supply a valid project[/red]")
    exit()
cprint(f"[green]Project {sys.argv[1].upper()} selected[/green]")

# If the path isn't specified, go look for it
projpath = ""
if len(sys.argv) < 3:
    cprint(f"[yellow]No project path specified. Now searching for a folder named {sys.argv[1].upper()} up to {exercise['search_depth']} directories deep...[/yellow]")
    filtered = []
    pathoptions = []
    for depth in range(1, exercise["search_depth"]):
        possiblepaths = find_sub_dirs(f"/Users/{os.environ.get('USER')}", depth)
        possiblepaths = [a.lower() for a in possiblepaths]
        for path in possiblepaths:
            if "eval" not in path:
                filtered.append(path.lower())
    for pathroot in filtered:
        if pathroot.split("/")[-2] == sys.argv[1].lower():
            pathoptions.append(pathroot)
    if len(pathoptions) == 0:
        cprint(f"[red]Could not find a folder named {sys.argv[1].upper()}[/red]")
        exit()
    if len(pathoptions) == 1:
        projpath = pathoptions[0]
    else:
        cprint("[yellow]Multiple possible paths found[/yellow]")
        for x in range(len(pathoptions)):
            cprint(f"[green]{x}: {pathoptions[x]}[/green]")
        cprint(f"[yellow]Please select an option by entering a number from 0 to {len(pathoptions) - 1}[/yellow]")
        inp = input("> ")
        try:
            projpath = pathoptions[int(inp)]
        except:
            cprint(f"[red]Invalid input {inp}[/red]")
            exit()
# Path is specified, validate it
else:
    if os.path.isdir(sys.argv[2]):
        projpath = sys.argv[2]
    elif os.path.isdir(f"/Users/{os.environ.get('USER')}/{sys.argv[2]}"):
        projpath = f"/Users/{os.environ.get('USER')}/{sys.argv[2]}"
    else:
        cprint(f"[red]Path {sys.argv[2]} not found[/red]")
        exit()
cprint(f"[green]Project path: {projpath}[/green]")
project = sys.argv[1].lower()
configs = {}
i = 0
for exerciseconfig in projectconfigs[project]:
    configs["ex" + str(i) if i > 9 else "ex0" + str(i)] = exerciseconfig
    i += 1

todel = []
cprint(f"[green]{len(configs)} exercise configs loaded[/green]")
for exercise in configs:
    if not os.path.isdir(projpath + "/" + exercise):
        cprint(f"[red]Exercise folder {exercise} could not be found[/red]")
        todel.append(exercise)
for x in todel:
    del configs[x]

import json
import os
import re
import sys
from glob import glob
from pathlib import Path
from ctypes import cdll, c_byte, c_int, c_char_p, c_void_p
from wurlitzer import pipes

from rich import print as cprint

def output(passed: bool, fname: str, inp: str, expected: str, actual: str):
	if inp == "\n":
		inp = "\\\n"
	if passed:
		if inp != "":
			cprint(f"[green]Pass: {fname} | Input: {inp} | Result: {expected}[/green]")
		else:
			cprint(f"[green]Pass: {fname} | Result: {expected}[/green]")
	else:
		if inp != "":
			cprint(f"[red]Fail: {fname} | Input: {inp} | Expected: {expected} | Result: {actual}[/red]")
		else:
			cprint(f"[red]Fail: {fname} | Expected: {expected} | Result: {actual}[/red]")

def getreturntype(t: str):
	if t == "char":
		return c_byte
	if t == "int":
		return c_int
	if t == "str":
		return c_char_p
	if t == "void":
		return c_void_p


def test(exercise_folder: str, fname: str):
	if not os.path.isfile(f"{exercise_folder}/{fname}.c"):
		cprint(f"[red]File not found: {exercise_folder}/{fname}.c[/red]")
	with pipes() as (out, err):
		if os.path.isfile(f"/Users/{os.environ.get('USER')}/42Tester/out/{fname}.o"):
			os.system(f"rm /Users/{os.environ.get('USER')}/42Tester/out/{fname}.o")
		ret = os.system(f"cc -Wall -Werror -Wextra -shared -o /Users/{os.environ.get('USER')}/42Tester/out/{fname}.o -fPIC {exercise_folder}/{fname}.c")
	if ret != 0:
		cprint(f"[red]Compile failed for {fname}.c[/red]")
		print(err.read())
		return False
	objfile = cdll.LoadLibrary(f"/Users/{os.environ.get('USER')}/42Tester/out/{fname}.o")
	moduleloc = f"/Users/{os.environ.get('USER')}/42Tester/tests/{exercise_folder.split('/')[-2]}/{fname}.py"
	if not os.path.isfile(moduleloc):
		cprint(f"[red]Test file for {fname} does not exist! If this is an error please report it[/red]")
		exit()
	tester = getattr(__import__(f"tests.{exercise_folder.split('/')[-2]}.{fname}"), exercise_folder.split('/')[-2])
	getattr(tester, fname).runtest(objfile)

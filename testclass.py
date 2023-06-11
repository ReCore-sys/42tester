from rich import print as cprint

def output(passed: bool, inp: str, expected: str, actual: str):
	if inp == "\n":
		inp = "<newline>"
	if passed:
		if inp != "":
			cprint(f"[green]Pass | Input: {inp} | Result: {expected}[/green]")
		else:
			cprint(f"[green]Pass | Result: {expected}[/green]")
	else:
		if inp != "":
			cprint(f"[red]Fail | Input: {inp} | Expected: {expected} | Result: {actual}[/red]")
		else:
			cprint(f"[red]Fail | Expected: {expected} | Result: {actual}[/red]")

class TestOutput():
	exercise = "None"
	project = "None"
	def __init__(self, exercise, project):
		self.excerise = exercise
		self.project = project
		cprint(f"\n[blue]Starting tests for {self.project} | {self.excerise.upper()}[/blue]\n")

	def runtest(self, target, actual, inp = None, hideout = False):
		passed = target == actual
		output(passed, "" if inp == None else inp, target if not hideout else "<Output Hidden>", actual)


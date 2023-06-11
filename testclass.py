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
	total = 0
	notfailed = 0
	def __init__(self, exercise, project):
		self.excerise = exercise
		self.project = project
		cprint(f"\n[blue]Starting tests for {self.project} | {self.excerise.upper()}[/blue]\n")

	def runtest(self, target, actual, inp = None, hideout = False):
		passed = target == actual
		self.total += 1
		if passed:
			self.notfailed += 1
		output(passed, "" if inp == None else inp, target if not hideout else "<Output Hidden>", actual if not hideout else "<Output Hidden>")
	
	def __enter__(self):
		return self
	
	def __exit__(self, *args):
		if self.total == self.notfailed:
			cprint(f"\n[green]{self.total}/{self.total} tests passed for {self.project}-{self.excerise.upper()}[/green]")
		else:
			cprint(f"\n[red]{self.notfailed}/{self.total} tests passed for {self.project}-{self.excerise.upper()}[/red]")


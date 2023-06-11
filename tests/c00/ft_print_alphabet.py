from testclass import TestOutput
from wurlitzer import pipes

import sys
def runtest(obj):
	with TestOutput("ex01", "C00") as test:
		with pipes() as (out, err):
			obj.ft_print_alphabet()
		test.runtest("abcdefghijklmnopqrstuvwxyz", out.read())
	
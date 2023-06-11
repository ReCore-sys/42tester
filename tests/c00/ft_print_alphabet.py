from testclass import TestOutput
from wurlitzer import pipes

import sys
def runtest(obj):
	test = TestOutput("ex01", "C00")
	with pipes() as (out, err):
		obj.ft_print_alphabet()
	test.runtest("abcdefghijklmnopqrstuvwxyz", out.read())
	
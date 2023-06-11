from testclass import TestOutput
from wurlitzer import pipes

import sys
def runtest(obj):
	with TestOutput("ex08", "C00") as test:
		with pipes() as (out, err):
			obj.ft_print_combn(2)
		test.runtest("01, ", out.read()[:4])
		with pipes() as (out, err):
			obj.ft_print_combn(2)
		test.runtest(", 89", out.read()[-4:])
		with pipes() as (out, err):
			obj.ft_print_combn(3)
		test.runtest("012, ", out.read()[:5])
		with pipes() as (out, err):
			obj.ft_print_combn(3)
		test.runtest(", 789", out.read()[-5:])
	
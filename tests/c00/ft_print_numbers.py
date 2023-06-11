from testclass import TestOutput
from wurlitzer import pipes

import sys
def runtest(obj):
	test = TestOutput("ex03", "C00")
	with pipes() as (out, err):
		obj.ft_print_numbers()
	test.runtest("0123456789", out.read())
	
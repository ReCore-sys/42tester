from testclass import TestOutput
from wurlitzer import pipes

import sys
def runtest(obj):
	with TestOutput("ex04", "C00") as test:
		with pipes() as (out, err):
			obj.ft_is_negative(5)
		test.runtest("P", out.read(), 5)	
		with pipes() as (out, err):
			obj.ft_is_negative(-5)
		test.runtest("N", out.read(), -5)	
		with pipes() as (out, err):
			obj.ft_is_negative(0)
		test.runtest("P", out.read(), 0)
	
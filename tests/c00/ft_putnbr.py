from testclass import TestOutput
from wurlitzer import pipes

import sys
def runtest(obj):
	with TestOutput("ex07", "C00") as test:
		with pipes() as (out, err):
			obj.ft_putnbr(5)
		test.runtest("5", out.read())
		with pipes() as (out, err):
			obj.ft_putnbr(-10)
		test.runtest("-10", out.read())
		with pipes() as (out, err):
			obj.ft_putnbr(0)
		test.runtest("0", out.read())
	
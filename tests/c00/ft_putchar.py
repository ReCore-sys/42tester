from testclass import TestOutput
from wurlitzer import pipes

import sys
def runtest(obj):
	test = TestOutput("ex00", "C00")
	with pipes() as (out, err):
		obj.ft_putchar(str.encode("a")[0])
	test.runtest("a", out.read())
	with pipes() as (out, err):
		obj.ft_putchar(str.encode("Z")[0])
	test.runtest("Z", out.read())
	with pipes() as (out, err):
		obj.ft_putchar(str.encode("d")[0])
	test.runtest("d", out.read())
	
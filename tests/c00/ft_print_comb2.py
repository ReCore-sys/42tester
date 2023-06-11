from testclass import TestOutput
from wurlitzer import pipes

import sys

def runtest(obj):
	with TestOutput("ex06", "C00") as test:
		with pipes() as (out, err):
			obj.ft_print_comb2()
		actual = out.read()
		test.runtest("00 01,", actual[:6])
		test.runtest(", 98 99", actual[-7:])
		test.runtest(34648, len(actual))
		test.runtest("0 08, 00 0", actual[50:60])
	
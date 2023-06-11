from testclass import TestOutput
from wurlitzer import pipes

import sys
def runtest(obj):
	with TestOutput("ex02", "C00") as test:
		with pipes() as (out, err):
			obj.ft_print_reverse_alphabet()
		test.runtest("zyxwvutsrqponmlkjihgfedcba", out.read())
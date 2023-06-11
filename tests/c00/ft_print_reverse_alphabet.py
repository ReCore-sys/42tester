from testclass import TestOutput
from wurlitzer import pipes

import sys
def runtest(obj):
	test = TestOutput("ex02", "C00")
	with pipes() as (out, err):
		obj.ft_print_reverse_alphabet()
	test.runtest("zyxwvutsrqponmlkjihgfedcba", out.read())
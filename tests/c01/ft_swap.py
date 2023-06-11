from testclass import TestOutput
from wurlitzer import pipes
import ctypes as ct
from rich import print as cprint

import sys
def runtest(obj):
	with TestOutput("ex02", "C01") as test:
		obj.ft_swap.argtypes = (ct.POINTER(ct.c_int),ct.POINTER(ct.c_int))
		a = ct.c_int(12)
		b = ct.c_int(42)
		obj.ft_swap(ct.byref(a), ct.byref(b))
		test.runtest(12, b.value)
		test.runtest(42, a.value)
		a = ct.c_int(500)
		b = ct.c_int(-2)
		obj.ft_swap(ct.byref(a), ct.byref(b))
		test.runtest(500, b.value)
		test.runtest(-2, a.value)
		a = ct.c_int(0)
		b = ct.c_int(0)
		obj.ft_swap(ct.byref(a), ct.byref(b))
		test.runtest(0, b.value)
		test.runtest(0, a.value)

	
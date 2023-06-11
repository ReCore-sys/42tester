from testclass import TestOutput
from wurlitzer import pipes
import ctypes as ct
from rich import print as cprint

import sys
def runtest(obj):
	with TestOutput("ex02", "C01") as test:
		obj.ft_div_mod.argtypes = (ct.c_int, ct.c_int, ct.POINTER(ct.c_int),ct.POINTER(ct.c_int))
		a = ct.c_int(50)
		b = ct.c_int(8)
		div = ct.c_int(0)
		mod = ct.c_int(0)
		obj.ft_div_mod(a, b, ct.byref(div), ct.byref(mod))
		test.runtest(6, div.value)
		test.runtest(50 % 8, mod.value)
		a = ct.c_int(10)
		b = ct.c_int(5)
		div = ct.c_int(0)
		mod = ct.c_int(0)
		obj.ft_div_mod(a, b, ct.byref(div), ct.byref(mod))
		test.runtest(2, div.value)
		test.runtest(0, mod.value)
		a = ct.c_int(13)
		b = ct.c_int(2)
		div = ct.c_int(0)
		mod = ct.c_int(0)
		obj.ft_div_mod(a, b, ct.byref(div), ct.byref(mod))
		test.runtest(6, div.value)
		test.runtest(1, mod.value)

	
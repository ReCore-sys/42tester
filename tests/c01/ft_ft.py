from testclass import TestOutput
from wurlitzer import pipes
import ctypes as ct

import sys
def runtest(obj):
	with TestOutput("ex00", "C01") as test:
		obj.ft_ft.argtypes = (ct.POINTER(ct.c_int),)
		passval = ct.c_int(100)
		obj.ft_ft(ct.byref(passval))
		test.runtest(42, passval.value)
	
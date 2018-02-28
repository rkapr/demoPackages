#!/usr/bin/env python
##cython: language_level=3

import ctypes
import ctypes.util

#_libfib = ctypes.cdll.LoadLibrary(find_library('fib.dylib'))
_libfib = ctypes.cdll.LoadLibrary("./fib.so")

def fib1(a):
    # print("Inside fib.py")
    return _libfib.fib(ctypes.c_int(a))

## Compile with gcc -dynamiclib fib.c -o fib.dylib

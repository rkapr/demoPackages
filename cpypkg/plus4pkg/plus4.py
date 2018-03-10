import ctypes
import ctypes.util

# Uncomment line below when importing as package
#_libfib = ctypes.cdll.LoadLibrary(ctypes.util.find_library('_plus.so'))
# Uncomment line below when running in ipython
_libfib = ctypes.cdll.LoadLibrary("./plus4pkg/_plus.so")

def plus4_func(a):
    return _libfib.plus4Cfunc(ctypes.c_int(a))
# Compile on MAC:

# gcc -shared -fPIC -o _plus.so plus4.c

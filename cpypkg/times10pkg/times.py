import ctypes
import ctypes.util

# Uncomment line below when running in jupyter notebook
#_libfib = ctypes.cdll.LoadLibrary(ctypes.util.find_library('_times.so'))
# Uncomment line below when running in ipython
_libfib = ctypes.cdll.LoadLibrary("./times10pkg/_times.so")

def times10(a):
    return _libfib.times10(ctypes.c_int(a))
# Compile on MAC:
# gcc -fPIC -O2 -c times10.c
# gcc -shared times10.o -o _times.so


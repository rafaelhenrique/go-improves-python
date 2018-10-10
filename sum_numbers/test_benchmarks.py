from ctypes import POINTER, Structure, c_longlong, c_void_p, cdll

from gosum_module import SumSlicePy


class GoSlice(Structure):
    _fields_ = [("data", POINTER(c_void_p)),
                ("len", c_longlong), ("cap", c_longlong)]


def List(seq):
    size = len(seq)
    return GoSlice((c_void_p * size)(*seq), size, size)


gosum = cdll.LoadLibrary("./gosum.so")
gosum.SumSlice.argtypes = [GoSlice]
gosum.SumSlice.restype = c_longlong


#
# Benchmark tests
#

def test_python_sum(benchmark, numbers):
    """Built-in Python sum function"""
    benchmark(sum, numbers)


def test_golang_ctypes_sum(benchmark, numbers):
    """Using SumSlice by ctypes"""
    benchmark(gosum.SumSlice, List(numbers))


def test_golang_module_sum(benchmark, numbers):
    """Using SumSlicePy by gosum_module"""
    benchmark(SumSlicePy, numbers)

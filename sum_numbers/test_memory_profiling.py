from ctypes import POINTER, Structure, c_longlong, c_void_p, cdll

from memory_profiler import profile

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
# Memory profiling tests
#

@profile
def python_sum_result(numbers):
    return sum(numbers)


@profile
def golang_ctypes_sum_result(numbers):
    return gosum.SumSlice(List(numbers))


@profile
def golang_module_sum_result(numbers):
    return SumSlicePy(numbers)


if __name__ == '__main__':
    numbers = range(0, 100)
    python_sum_result(numbers)
    golang_ctypes_sum_result(numbers)
    golang_module_sum_result(numbers)

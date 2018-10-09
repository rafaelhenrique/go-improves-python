from ctypes import POINTER, Structure, c_longlong, c_void_p, cdll

import pytest
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


@pytest.fixture
def numbers():
    return range(0, 100)


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


#
# Common tests
#


def test_python_sum_result(numbers):
    assert sum(numbers) == 4950


def test_golang_ctypes_sum_result(numbers):
    assert gosum.SumSlice(List(numbers)) == 4950


def test_golang_module_sum_result(numbers):
    assert SumSlicePy(numbers) == 4950


if __name__ == '__main__':
    numbers = numbers()
    python_sum_result(numbers)
    golang_ctypes_sum_result(numbers)
    golang_module_sum_result(numbers)

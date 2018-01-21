from gosum_module import SumSlicePy

numbers = range(0, 100)


def test_builtin_sum(benchmark):
    benchmark(sum, numbers)


def test_golang_sum(benchmark):
    benchmark(SumSlicePy, numbers)

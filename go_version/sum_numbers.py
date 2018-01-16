from gosum import SumSlicePy

numbers = range(0, 10)


def test_sum(benchmark):
    benchmark(sum, list(numbers))
    benchmark(SumSlicePy, list(numbers))


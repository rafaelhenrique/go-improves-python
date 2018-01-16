
numbers = range(0, 100000000)


def test_sum(benchmark):
    benchmark(sum, numbers)

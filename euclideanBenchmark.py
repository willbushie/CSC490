# continued class programming from 2-1-2022

# import necessary things
import timeit
from memory_profiler import profile
import requests

# implementing the euclidean code

# loop
def loop(m, n):
    if (m == 0):
        return n
    l = n % m
    while (l > 0):
        n = m
        m = l
        l = n % m
    return m

# recursion
def recursive(m,n):
    if (m == 0):
        return n
    else:
        l = n % m
        n = m
        m = l
        return recursive(m, n)

# used for benchmarking loop using timeit
def test_loop():
    loop(9987654321,1123456789)
# used for benchmarking recursion using timeit
def test_recursion():
    recursive(9987654321,1123456789)

# benchmark using timeit
def benchmark1():
    # calling the methods
    print("loop:")
    print(timeit.Timer(test_loop).timeit(number=100))
    print("recursion:")
    print(timeit.Timer(test_recursion).timeit(number=100))

# benchmark using line_profiler 
@profile
def benchmark2a():
    for i in range(1000):
        test_loop()

@profile
def benchmark2b():
    for i in range(1000):
        test_recursion()


# calling benchmark1 (timeit)
benchmark1()

# calling benchmarks 2a & 2b (line_profiler)
benchmark2a()
benchmark2b()

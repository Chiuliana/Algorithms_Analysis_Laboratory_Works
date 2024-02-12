import math
import time
import matplotlib.pyplot as plt
import sys
from tabulate import tabulate

sys.setrecursionlimit(1000000)
firstSeries = [5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30, 32, 35, 37, 40, 42, 45]
secondSeries = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]

class FibonacciAlgorithms:
    def fib_recursive(self, n):
        if n <= 1:
            return n
        else:
            return self.fib_recursive(n-1) + self.fib_recursive(n-2)

    def fib_iterative(self, n):
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return a

    def fib_matrix_exponentiation(self, n):
        if n <= 1:
            return n

        def multiply(A, B):
            return [[A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
                    [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]]

        def power_matrix(matrix, n):
            if n == 1:
                return matrix
            elif n % 2 == 0:
                half_power = power_matrix(matrix, n // 2)
                return multiply(half_power, half_power)
            else:
                return multiply(matrix, power_matrix(matrix, n - 1))

        fib_matrix = [[1, 1], [1, 0]]
        result_matrix = power_matrix(fib_matrix, n - 1)
        return result_matrix[0][0]

    def fib_binet(self, n):
        sqrt_5 = int(math.sqrt(5))
        phi = (1 + sqrt_5) // 2
        psi = (1 - sqrt_5) // 2
        return int((phi ** n - psi ** n) // sqrt_5)

    def fib_memoization(self, n, memo=None):
        if memo is None:
            memo = {}
        if n in memo:
            return memo[n]
        if n <= 1:
            return n
        memo[n] = self.fib_memoization(n - 1, memo) + self.fib_memoization(n - 2, memo)
        return memo[n]

    def fib_bottom_up(self, n):
        if n <= 1:
            return n
        fib = [0] * (n + 1)
        fib[1] = 1
        for i in range(2, n + 1):
            fib[i] = fib[i - 1] + fib[i - 2]
        return fib[n]

fib_alg = FibonacciAlgorithms()


def test_and_plot_algorithms(input_data, algorithm_names, algorithms):
    times = {name: [] for name in algorithm_names}
    for n in input_data:
        for name, function in algorithms:
            start = time.perf_counter()
            function(n)
            end = time.perf_counter()
            times[name].append(end - start)

    for name, times_list in times.items():
        plt.plot(input_data, times_list, label=name)
    plt.xlabel('Input Size')
    plt.ylabel('Time')
    plt.title('Execution Time')
    plt.legend()
    plt.show()

    data = [[n] + [times[name][i] for name in algorithm_names] for i, n in enumerate(input_data)]
    headers = ["Input Size"] + algorithm_names
    print(tabulate(data, headers=headers, tablefmt="fancy_grid"))


algorithm_names = ["Recursive", "Iterative", "Matrix", "Memoization", "Binet", "Bottom Up"]
algorithms = [
    ("Recursive", fib_alg.fib_recursive),
    ("Iterative", fib_alg.fib_iterative),
    ("Matrix", fib_alg.fib_matrix_exponentiation),
    ("Binet", fib_alg.fib_binet),
    ("Memoization", fib_alg.fib_memoization),
    ("Bottom Up", fib_alg.fib_memoization)
]

# Test and plot algorithms for the first input
test_and_plot_algorithms(firstSeries, algorithm_names, algorithms)

# Test and plot algorithms for the second input
test_and_plot_algorithms(secondSeries, algorithm_names[1:], algorithms[1:])
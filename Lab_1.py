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
#test_and_plot_algorithms(firstSeries, algorithm_names, algorithms)

# Test and plot algorithms for the second input
#test_and_plot_algorithms(secondSeries, algorithm_names[1:], algorithms[1:])


def test_and_plot_algorithm(input_data, algorithm_name, algorithm_func):
    times = []
    for n in input_data:
        start = time.perf_counter()
        algorithm_func(n)
        end = time.perf_counter()
        times.append(end - start)

    plt.plot(input_data, times, label=algorithm_name)
    plt.xlabel('Input Size')
    plt.ylabel('Time')
    plt.title(f'Execution Time for {algorithm_name}')
    plt.legend()
    plt.show()

    data = [[n, time] for n, time in zip(input_data, times)]
    headers = ["Input Size", "Time"]
    print(tabulate(data, headers=headers, tablefmt="fancy_grid"))

# Test and plot just the Recursive algorithm for the first input
test_and_plot_algorithm(firstSeries, "Recursive", fib_alg.fib_recursive)

# Display results in a table for the Recursive algorithm for the first input
data = []
for n in firstSeries:
    start_time = time.perf_counter()
    fib_alg.fib_recursive(n)
    end_time = time.perf_counter()
    data.append([n, end_time - start_time])
headers = ["Input Size", "Time"]
print("Table result for Recursive Algorithm (First Input):")
print(tabulate(data, headers=headers, tablefmt="fancy_grid"))

# # Test and plot just the iterative algorithm for the first input
# test_and_plot_algorithm(secondSeries, "Iterative", fib_alg.fib_iterative)
#
# # Display results in a table for the iterative algorithm for the first input
# data = []
# for n in secondSeries:
#     start_time = time.perf_counter()
#     fib_alg.fib_iterative(n)
#     end_time = time.perf_counter()
#     data.append([n, end_time - start_time])
#
# headers = ["Input Size", "Time"]
# print("Table result for Iterative Algorithm (Second Input):")
# print(tabulate(data, headers=headers, tablefmt="fancy_grid"))
#
#
# # Test and plot just the matrix exponentiation algorithm for the second input
# test_and_plot_algorithm(secondSeries, "Matrix Exponentiation", fib_alg.fib_matrix_exponentiation)
#
# # Display results in a table for the matrix exponentiation algorithm for the second input
# data = []
# for n in secondSeries:
#     start_time = time.perf_counter()
#     fib_alg.fib_matrix_exponentiation(n)
#     end_time = time.perf_counter()
#     data.append([n, end_time - start_time])
#
# print("Table result for Matrix Exponentiation Algorithm (Second Input):")
# print(tabulate(data, headers=headers, tablefmt="fancy_grid"))
#
#
# # Test and plot just the Binet algorithm for the second input
# test_and_plot_algorithm(secondSeries, "Binet", fib_alg.fib_binet)
#
# # Display results in a table for the Binet algorithm for the second input
# data = []
# for n in secondSeries:
#     start_time = time.perf_counter()
#     fib_alg.fib_binet(n)
#     end_time = time.perf_counter()
#     data.append([n, end_time - start_time])
#
# print("Table result for Binet Algorithm (Second Input):")
# print(tabulate(data, headers=headers, tablefmt="fancy_grid"))
#
# # Test and plot just the Memoization algorithm for the second input
# test_and_plot_algorithm(secondSeries, "Memoization", fib_alg.fib_memoization)
#
# # Display results in a table for the Memoization algorithm for the second input
# data = []
# for n in secondSeries:
#     start_time = time.perf_counter()
#     fib_alg.fib_memoization(n)
#     end_time = time.perf_counter()
#     data.append([n, end_time - start_time])
#
# print("Table result for Memoization Algorithm (Second Input):")
# print(tabulate(data, headers=headers, tablefmt="fancy_grid"))
#
# # Test and plot just the Bottom Up algorithm for the second input
# test_and_plot_algorithm(secondSeries, "Bottom Up", fib_alg.fib_bottom_up)
#
# # Display results in a table for the Bottom Up algorithm for the second input
# data = []
# for n in secondSeries:
#     start_time = time.perf_counter()
#     fib_alg.fib_bottom_up(n)
#     end_time = time.perf_counter()
#     data.append([n, end_time - start_time])
#
# print("Table result for Bottom Up Algorithm (Second Input):")
# print(tabulate(data, headers=headers, tablefmt="fancy_grid"))


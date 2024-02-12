import math
# Recursive Algorithm
def fib_recursive(n):
    if n <= 1:
        return n
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

# Iterative Algorithm
def fib_iterative(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

# Matrix exponentiation Algorithm
def fib_matrix_exponentiation(n):
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

# Binet's formula Algorithm
def fib_binet(n):
    sqrt_5 = int(math.sqrt(5))
    phi = (1 + sqrt_5) // 2
    psi = (1 - sqrt_5) // 2
    return int((phi ** n - psi ** n) // sqrt_5)

# Memoization Algorithm
def fib_memoization(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memoization(n - 1, memo) + fib_memoization(n - 2, memo)
    return memo[n]

# Bottom-up dynamic programming Algorithm
def fib_bottom_up(n):
    if n <= 1:
        return n
    fib = [0] * (n + 1)
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]


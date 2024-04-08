#9! = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9

def factorial(n):
    if n == 1:
        return 1
    factorial_n_minus_1 = factorial(n=n - 1)
    return n * factorial_n_minus_1

print(factorial(1000))
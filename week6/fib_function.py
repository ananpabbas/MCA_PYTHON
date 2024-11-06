
def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

n_terms=int(input("enter the number of terms in the fibonacci series"))
result = fibonacci(n_terms)
print(f"Fibonacci series with {n_terms} terms: {result}")

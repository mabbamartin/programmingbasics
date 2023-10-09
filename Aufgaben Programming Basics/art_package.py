fib = (lambda f: (lambda x: x(x))(lambda y: f(lambda *args: y(y)(*args))))(lambda f: lambda n: 0 if n == 0 else 1 if n == 1 else f(n-1) + f(n-2))

print([fib(i) for i in range(10)])  # Outputs the first 10 Fibonacci numbers

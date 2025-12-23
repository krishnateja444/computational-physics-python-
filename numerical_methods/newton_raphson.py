def newton_raphson(f, df, x0, iterations=10):
    x = x0
    for _ in range(iterations):
        x = x - f(x) / df(x)
    return x

# Example: Solve x^2 - 2 = 0
f = lambda x: x**2 - 2
df = lambda x: 2*x

root = newton_raphson(f, df, 1.0)
print("Root:", root)

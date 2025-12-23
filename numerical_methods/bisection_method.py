def bisection(f, a, b, tol=1e-6):
    while abs(b - a) > tol:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

f = lambda x: x**3 - x - 2
root = bisection(f, 1, 2)
print("Root:", root)

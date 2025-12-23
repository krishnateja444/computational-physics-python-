def euler_method(f, y0, t0, t_end, h):
    t = t0
    y = y0
    while t <= t_end:
        print(f"t={t:.2f}, y={y:.4f}")
        y += h * f(t, y)
        t += h

# dy/dt = -2y
f = lambda t, y: -2*y
euler_method(f, 1, 0, 1, 0.1)

x = list(map(float, input("Enter x values: ").split()))
y = list(map(float, input("Enter y values: ").split()))

n = len(x)

x_bar = sum(x)/n
y_bar = sum(y)/n

m = sum((x[i] - x_bar) * (y[i] - y_bar) for i in range(n)) / sum((x[i] - x_bar) ** 2 for i in range(n))

b = y_bar - m*x_bar

print("Slope (m):", m)
print("Intercept (b):", b)
print(f"Equation of line: y = {m:.4f}x + {b:.4f}")
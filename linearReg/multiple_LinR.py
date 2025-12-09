n = int(input("Enter number of observations: "))

X1 = []
X2 = []
Y  = []

print("\nEnter values for X1, X2, Y:")
for i in range(n):
    x1 = float(input(f"X1[{i+1}]: "))
    x2 = float(input(f"X2[{i+1}]: "))
    y  = float(input(f"Y[{i+1}]: "))
    X1.append(x1)
    X2.append(x2)
    Y.append(y)
    print()

sum_x1 = sum(X1)
sum_x2 = sum(X2)
sum_y  = sum(Y)

sum_x1_sq = sum([x*x for x in X1])
sum_x2_sq = sum([x*x for x in X2])

sum_x1_x2 = sum([X1[i] * X2[i] for i in range(n)])
sum_x1_y  = sum([X1[i] * Y[i]  for i in range(n)])
sum_x2_y  = sum([X2[i] * Y[i]  for i in range(n)])

D = (sum_x1_sq * sum_x2_sq) - (sum_x1_x2 ** 2)

beta1 = ((sum_x2_sq * sum_x1_y) - (sum_x1_x2 * sum_x2_y)) / D
beta2 = ((sum_x1_sq * sum_x2_y) - (sum_x1_x2 * sum_x1_y)) / D

x1_bar = sum_x1 / n
x2_bar = sum_x2 / n
y_bar  = sum_y / n

beta0 = y_bar - beta1 * x1_bar - beta2 * x2_bar

print("\nRegression Coefficients:")
print("β0 (Intercept) = ", beta0)
print("β1 (Coefficient for X1) =", beta1)
print("β2 (Coefficient for X2) =", beta2)
def T(n, x):
    if n == 0:
        return 1
    if n == 1:
        return x
    if n > 1:
        return 2 * x * T(n-1, x) - T(n-2, x)

y = list(map(int,input().split()))
print(T(y[0], y[1]))


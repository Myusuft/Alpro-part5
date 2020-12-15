import sys
def f(n):
    if n == 0:
        return 10
    if n >= 0 and n%2 == 0:
        return 4* f(n/2)
    if n >= 1 and n%2 != 0:
        return  f(n-1) +1
n = int(input())
sys.stdout.write(str(f(n)))
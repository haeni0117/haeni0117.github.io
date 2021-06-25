def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num


a = int(input())

for _ in range(a):
    n, m = map(int, input().split())
    l = factorial(m) // (factorial(n) * factorial(m - n))
    print(l)
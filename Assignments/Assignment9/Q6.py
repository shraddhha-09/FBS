def fib(a, b, n):
    if n == 0:
        return
    print(a, end=" ")
    fib(b, a+b, n-1)

n = int(input("Enter terms: "))
fib(0, 1, n)

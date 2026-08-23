def fact(x):
    f = 1
    for i in range(1, x+1):
        f *= i
    return f

def fact_sum(n):
    s = 0
    for i in range(1, n+1):
        s += fact(i)
    return s

n = int(input("Enter n: "))
print("Sum =", fact_sum(n))

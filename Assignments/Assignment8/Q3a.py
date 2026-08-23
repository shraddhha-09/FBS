def series_sum(n):
    s = 0
    for i in range(1, n+1):
        s += i
    return s

n = int(input("Enter n: "))
print("Sum =", series_sum(n))

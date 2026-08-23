def power_sum(n):
    s = 0
    for i in range(1, n+1):
        s += i**i
    return s

n = int(input("Enter n: "))
print("Sum =", power_sum(n))

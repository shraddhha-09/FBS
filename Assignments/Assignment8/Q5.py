def is_prime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def prime_sum(n):
    s = 0
    for i in range(1, n+1):
        if is_prime(i):
            s += i
    return s

n = int(input("Enter n: "))
print("Sum =", prime_sum(n))

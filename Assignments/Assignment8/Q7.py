def digit_sum(num):
    s = 0
    while num > 0:
        s += num % 10
        num //= 10
    return s

num = int(input("Enter number: "))
print("Sum =", digit_sum(num))

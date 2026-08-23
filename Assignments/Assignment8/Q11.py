def is_armstrong(num):
    s = 0
    temp = num
    d = len(str(num))
    while temp > 0:
        s += (temp%10)**d
        temp //= 10
    return s == num

num = int(input("Enter number: "))
print("Armstrong?", is_armstrong(num))

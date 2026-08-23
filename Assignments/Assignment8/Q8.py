def reverse(num):
    rev = 0
    while num > 0:
        rev = rev*10 + num%10
        num //= 10
    return rev

num = int(input("Enter number: "))
print("Reverse =", reverse(num))

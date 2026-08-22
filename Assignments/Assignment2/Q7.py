num = int(input("Enter 3 digit number: "))
s = (num//100) + (num//10 % 10) + (num % 10)
print("Sum of digits =", s)

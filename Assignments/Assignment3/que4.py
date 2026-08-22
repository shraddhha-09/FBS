a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a + b > c and b + c > a and a + c > b:
    print("Valid triangle")
else:
    print("Invalid triangle")
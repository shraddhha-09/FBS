m1 = float(input("Enter marks of Subject 1: "))
m2 = float(input("Enter marks of Subject 2: "))
m3 = float(input("Enter marks of Subject 3: "))
m4 = float(input("Enter marks of Subject 4: "))
m5 = float(input("Enter marks of Subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

print("Percentage =", percentage)

if percentage >= 75:
    print("First Class")
elif percentage >= 60:
    print("Second Class")
elif percentage >= 50:
    print("Third Class")
else:
    print("Fail")
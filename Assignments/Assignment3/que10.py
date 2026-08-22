gender = input("Enter gender (male/female): ")
age = int(input("Enter age: "))

if gender.lower() == "male":
    if age >= 21:
        print("Eligible for marriage")
    else:
        print("Not eligible for marriage")

elif gender.lower() == "female":
    if age >= 18:
        print("Eligible for marriage")
    else:
        print("Not eligible for marriage")

else:
    print("Invalid gender")
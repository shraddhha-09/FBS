total_amount = 0

for i in range(1, 6):

    age = int(input("Enter age of person " + str(i) + ": "))
    ticket = float(input("Enter ticket amount: "))

    if age < 12:
        amount = ticket - (ticket * 30 / 100)
        print("30% discount")

    elif age > 59:
        amount = ticket - (ticket * 50 / 100)
        print("50% discount")

    else:
        amount = ticket
        print("No discount")

    print("Amount to pay =", amount)

    total_amount = total_amount + amount

print("Total ticket amount =", total_amount)
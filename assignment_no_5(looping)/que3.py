n = int(input("Enter number of passengers: "))
ticket_cost = float(input("Enter ticket cost per person: "))

total_amount = 0

for i in range(1, n + 1):
    age = int(input("Enter age of passenger " + str(i) + ": "))

    if age < 12:
        amount = ticket_cost - (ticket_cost * 30 / 100)
        print("30% discount")
    
    elif age > 59:
        amount = ticket_cost - (ticket_cost * 50 / 100)
        print("50% discount")
    
    else:
        amount = ticket_cost
        print("No discount")

    print("Amount to pay =", amount)
    total_amount += amount

print("\nTotal amount to pay =", total_amount)
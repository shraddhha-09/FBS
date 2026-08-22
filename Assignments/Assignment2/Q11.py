amt = int(input("Enter amount: "))
notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
for n in notes:
    if amt >= n:
        count = amt // n
        amt = amt % n
        print(n, ":", count)

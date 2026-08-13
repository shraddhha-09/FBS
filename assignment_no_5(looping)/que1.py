i = 0
uid = int(input("Set ID:"))
upass = input("Set Password:")
while i < 4:
    id = int(input("Enter ID:"))
    password = input("Enter Password:")
    if id == uid and password == upass:
        break
    i += 1
import random

userid = input("Enter User ID: ")
password = input("Enter Password: ")

if userid == "admin" and password == "1234":

    captcha = random.randint(1000, 9999)

    print("Your CAPTCHA is:", captcha)

    entered = int(input("Enter CAPTCHA: "))

    if entered == captcha:
        print("Success! Login completed.")
    else:
        print("Failed! Incorrect CAPTCHA.")

else:
    print("Incorrect User ID or Password.")
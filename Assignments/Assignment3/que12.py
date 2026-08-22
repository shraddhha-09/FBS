num = int(input("Enter a 3 digit number: "))

if num < 100 or num > 999:
    print("Please enter a 3 digit number")
else:
    original = num

    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    if original == reverse:
        print("Palindrome number")
    else:
        print("Not a palindrome number")
def is_palindrome(num):
    return num == reverse(num)

num = int(input("Enter number: "))
print("Palindrome?", is_palindrome(num))

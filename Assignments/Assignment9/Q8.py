def is_prime(num, i=2):
    if num < 2:
        return False
    if i*i > num:
        return True
    if num % i == 0:
        return False
    return is_prime(num, i+1)

num = int(input("Enter number: "))
print("Prime?", is_prime(num))

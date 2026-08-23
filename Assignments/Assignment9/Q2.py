def armstrong(num, d):
    if num == 0:
        return 0
    return (num % 10)**d + armstrong(num//10, d)

num = int(input("Enter number: "))
d = len(str(num))
print("Armstrong?", armstrong(num, d) == num)

n = int(input("Enter number of students: "))

total_percentage = 0

for i in range(1, n + 1):
    print("\nEnter marks for Student", i)

    m1 = float(input("Subject 1 marks: "))
    m2 = float(input("Subject 2 marks: "))
    m3 = float(input("Subject 3 marks: "))
    m4 = float(input("Subject 4 marks: "))
    m5 = float(input("Subject 5 marks: "))

    total = m1 + m2 + m3 + m4 + m5
    percentage = (total / 500) * 100

    print("Percentage =", percentage, "%")

    total_percentage += percentage

average = total_percentage / n

print("\nAverage Percentage =", average, "%")
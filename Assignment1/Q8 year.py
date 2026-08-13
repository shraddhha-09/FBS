days=int(input("Enter Days:"))
year=days//365
days=days%365

weeks=days//365
days=days%7


print(f'{year}years,{weeks}weeks and {days}days')


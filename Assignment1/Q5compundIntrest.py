P=int(input('Enter principle:'))
R=float(input('Enter rate:'))
T=int(input('Enter Time:'))
A=P*(1+(R/100))**T
CI=A-P
print('Amount:',A)
print('Compound Intrest:',CI)

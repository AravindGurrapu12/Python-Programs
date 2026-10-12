# Factorial
n = int(input("Enter a number: "))
fact = 1

if n < 0:
    print("Enter a non-negative number")
else:
    for i in range(1, n + 1):
        fact *= i
    print("Factorial:", fact)

#Armstrong Number
n = int(input("Enter a number: "))
digits = str(n)
total = 0

for digit in digits:
    total += int(digit) ** len(digits)

if total == n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

#Patterns

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)
#Pascals Traingle

n = int(input("Enter rows: "))

for i in range(n):
    value = 1
    print(" " * (n - i), end="")

    for j in range(i + 1):
        print(value, end=" ")
        value = value * (i - j) // (j + 1)

    print()


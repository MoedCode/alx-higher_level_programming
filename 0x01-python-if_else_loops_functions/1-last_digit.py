#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Deigit = abs(number) % 10

print("Last digit of", number, "is", Deigit, end=" ")

if Deigit > 5:
    print("and is greater than 5")
elif Deigit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")


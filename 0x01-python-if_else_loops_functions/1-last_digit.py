#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Deigit = abs(number) % 10
if number < 0:
    Digit = -Digit
print("Last digit of {} is {} and is ".format(number, Deigit), end="")
if Deigit > 5:
    print("greater than 5")
elif Deigit == 0:
    print("0")
else:
    print("less than 6 and not 0")


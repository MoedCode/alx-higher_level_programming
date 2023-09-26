#!/usr/bin/python3
def fizzbuzz():
    """
    prints the numbers from 1 to 100 separated by a space
    multiples of three print Fizz instead of the number,
    for multiples of five print Buzz,For numbers which
    are multiples of both three and five print FizzBuzz.
    """

    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")

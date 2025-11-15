#!/usr/bin/python3

def print_last_digit(number):
    if number < 0:
        number *= -1
    return number % 10

if __name__ == "__main__":
    number = int(input())
    print("{:d}".format(print_last_digit(number)))

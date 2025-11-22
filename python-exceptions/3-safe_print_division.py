#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        res = a / b
        print("{}".format(res))
    except ZeroDivisionError:
        res = None
    finally:
        print("Inside result:", res)

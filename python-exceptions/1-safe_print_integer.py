#!/usr/bin/python3
idef safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False

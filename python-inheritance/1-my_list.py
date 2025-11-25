#!/usr/bin/python3
"""this is document """ 

class MyList(list):
    """this is document"""
    def __init__ (self, list = []):
        self.list = list
 """this is doucment"""

    def print_sorted(self):
        self.sort()
        print(self)

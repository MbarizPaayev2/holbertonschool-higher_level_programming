#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    #new_dic = {] 
     for key in a_dictionary.values():
        a_dictionary[key] = a_dictionary[key] * 2
    return a_dictionary

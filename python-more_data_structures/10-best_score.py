#!/usr/bin/python3
def best_score(a_dictionary):
    max = a_dictionary[0]
    for key in a_dictionary:
        if a_dictionary[key] > max:
            max = a_dictionary[key]
        
    if max == a_dictionary[0]:
        return None
    else:
        return max

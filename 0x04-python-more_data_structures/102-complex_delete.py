#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_to_remove = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            keys_to_remove.append(key)
    for key in keys_to_remove:
        del a_dictionary[key]
    return a_dictionary

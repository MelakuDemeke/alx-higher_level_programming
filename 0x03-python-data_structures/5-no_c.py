#!/usr/bin/python3
def no_c(my_string):
    without_c = [x for x in my_string if x != 'c' or x != 'C']
    return ("".join(without_c))

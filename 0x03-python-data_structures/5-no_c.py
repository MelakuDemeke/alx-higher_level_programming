#!/usr/bin/python3
def no_c(my_string):
    wthout_c = [x for x in my_string if x != 'c' or x != 'C']
    return("".join(wthout_c))

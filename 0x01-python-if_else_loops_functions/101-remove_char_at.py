#!/usr/bin/python3
def remove_char_at(str, n):
    update = ""
    i = 0
    for c in str:
        if i != n:
            update += c
        i += 1
    return update

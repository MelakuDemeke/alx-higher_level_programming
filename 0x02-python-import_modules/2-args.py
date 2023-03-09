#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    start = 0
    ar = sys.argv
    length = len(ar) - 1
    if length == 0:
        print("{:d} arguments.".format(length))
    elif length == 1:
        print("{:d} argument:".format(length))
    else:
        print("{:d} arguments:".format(length))
    for a in range(length):
        print("{:d}: {}".format(a + 1, sys.argv[a + 1]))

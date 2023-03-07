#!/usr/bin/python3
for letter in range(ord('z'), ord('a') - 1, -1):
    print("{:c}".format((letter - (ord('a') - ord('A'))) if letter % 2 else letter), end='')

#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul,div
    import sys

    alen = len(sys.argv)

    if alen != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    oprator = sys.argv[2]
    first_num = int(sys.argv[1])
    second_num = int(sys.argv[3])

    if oprator == "+":
        print("{} {} {} = {}".format(first_num, oprator, second_num, add(first_num, second_num)))
    elif oprator == "-":
        print("{} {} {} = {}".format(first_num, oprator, second_num, sub(first_num, second_num)))
    elif oprator == "*":
        print("{} {} {} = {}".format(first_num, oprator, second_num, mul(first_num, second_num)))
    elif oprator == "/":
        print("{} {} {} = {}".format(first_num, oprator, second_num, div(first_num, second_num)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        quit(1)

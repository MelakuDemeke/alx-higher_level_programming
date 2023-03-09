#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    alen = len(sys.argv)

    if alen != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    oprator = sys.argv[2]
    f_num = int(sys.argv[1])
    s_num = int(sys.argv[3])

    if oprator == "+":
        print("{} {} {} = {}".format(f_num, oprator, s_num, add(f_num, s_num)))
    elif oprator == "-":
        print("{} {} {} = {}".format(f_num, oprator, s_num, sub(f_num, s_num)))
    elif oprator == "*":
        print("{} {} {} = {}".format(f_num, oprator, s_num, mul(f_num, s_num)))
    elif oprator == "/":
        print("{} {} {} = {}".format(f_num, oprator, s_num, div(f_num, s_num)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        quit(1)

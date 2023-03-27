def safe_print_list_integers(my_list=[], x=0):
    printed = 0
    for i in range(x):
        try:
            print(f"{my_list[i]:d}", end="")
            printed += 1
        except (ValueError, TypeError):
            continue
    print()
    return (printed)

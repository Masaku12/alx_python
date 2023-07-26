for first_digit in range(10):
    for second_digit in range(first_digit + 1, 10):
        print("{}{}".format(first_digit, second_digit), end=", " if first_digit != 8 or second_digit != 9 else "\n")
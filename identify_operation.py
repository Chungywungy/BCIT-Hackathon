# assume that the function is split and each line of code is
# stored in a string inside a list, we loop
# so list[index] refers to each line in the string
# precondition : there is a white space around operators -saba

# i think += and -= should be in assignment instead of operators, im not going to move them this instant but
# this should be considered for making everything mesh in the future when we're refactoring this


def identify_operations(split_string):
    if "+=" in split_string:
        parts = split_string.split()
        addition_position = parts.index("+=")
        operand = parts[addition_position - 1]
        addition_value = parts[addition_position + 1]
        print("Increase {} by {}.".format(operand, addition_value))
        return "Increase {} by {}.".format(operand, addition_value)
    elif "+" in split_string:
        parts = split_string.split()
        addition_position = parts.index("+")
        first_operand = parts[addition_position - 1]
        second_operand = parts[addition_position + 1]
        print("Add {} with {}".format(first_operand, second_operand))
        return "Add {} with {}".format(first_operand, second_operand)
    elif "-=" in split_string:
        parts = split_string.split()
        subtraction_position = parts.index("-=")
        operand = parts[subtraction_position - 1]
        subtraction_value = parts[subtraction_position + 1]
        print("Decrease {} by {}.".format(operand, subtraction_value))
        return "Decrease {} by {}.".format(operand, subtraction_value)
    elif "-" in split_string:
        parts = split_string.split()
        subtraction_position = parts.index("-")
        first_operand = parts[subtraction_position - 1]
        second_operand = parts[subtraction_position + 1]
        print("Subtract {} from {}.".format(second_operand, first_operand))
        return "Subtract {} from {}.".format(second_operand, first_operand)
    elif "**=" in split_string:
        # we should do this first otherwise we're not getting into this block
        parts = split_string.split()
        multiply_position = parts.index("**=")
        first_operand = parts[multiply_position - 1]
        second_operand = parts[multiply_position + 1]
        print("Set {} to itself raised to the power of {}.".format(first_operand, second_operand))
        return "Set {} to itself raised to the power of {}.".format(first_operand, second_operand)
    elif "**" in split_string:
        parts = split_string.split()
        multiply_position = parts.index("**")
        first_operand = parts[multiply_position - 1]
        second_operand = parts[multiply_position + 1]
        print("Raise {} to the power of {}.".format(first_operand, second_operand))
        return "Raise {} to the power of {}.".format(first_operand, second_operand)
    elif "*=" in split_string:
        # *= and * are translated the same
        parts = split_string.split()
        multiply_position = parts.index("*=")
        first_operand = parts[multiply_position - 1]
        second_operand = parts[multiply_position + 1]
        print("Multiply {} by {}.".format(first_operand, second_operand))
        return "Multiply {} by {}.".format(first_operand, second_operand)
    elif "*" in split_string:
        # *= and * are translated the same
        parts = split_string.split()
        multiply_position = parts.index("*")
        first_operand = parts[multiply_position - 1]
        second_operand = parts[multiply_position + 1]
        print("Multiply {} with {}.".format(first_operand, second_operand))
        return "Multiply {} with {}.".format(first_operand, second_operand)
    elif "//" in split_string:
        #ordering matters cause if we put / before this, we never get to // block
        parts = split_string.split()
        int_division_position = parts.index("//")
        first_operand = parts[int_division_position - 1]
        second_operand = parts[int_division_position + 1]
        print("Divide {} by {}, rounding down to the nearest whole number.".format(first_operand, second_operand))
        return "Divide {} by {}, rounding down to the nearest whole number.".format(first_operand, second_operand)
    elif "/=" in split_string:
        parts = split_string.split()
        division_position = parts.index("/=")
        first_operand = parts[division_position - 1]
        second_operand = parts[division_position + 1]
        print("Divide {} by {}.".format(first_operand, second_operand))
        return "Divide {} by {}.".format(first_operand, second_operand)
    elif "/" in split_string:
        parts = split_string.split()
        division_position = parts.index("/")
        first_operand = parts[division_position - 1]
        second_operand = parts[division_position + 1]
        print("Divide {} with {}.".format(first_operand, second_operand))
        return "Divide {} with {}.".format(first_operand, second_operand)
    elif "%=" in split_string:
        parts = split_string.split()
        remainder_position = parts.index("%=")
        first_operand = parts[remainder_position - 1]
        second_operand = parts[remainder_position + 1]
        print("Set {} to the remainder when divided by {}.".format(first_operand, second_operand))
        return "Set {} to the remainder when divided by {}.".format(first_operand, second_operand)
    elif "%" in split_string:
        parts = split_string.split()
        modulo_position = parts.index("%")
        first_operand = parts[modulo_position - 1]
        second_operand = parts[modulo_position + 1]
        print("Find the remainder when {} is divided by {}.".format(first_operand, second_operand))
        return "Find the remainder when {} is divided by {}.".format(first_operand, second_operand)
    else:
        print(split_string)
        return split_string


def main():
    my_string = "x += y"
    identify_operations(my_string)
    my_second_string = "x + y"
    identify_operations(my_second_string)
    # this needs implementation, right now it assumes only singular operators. will refactor tmrw morning
    # VVV other than this, it functions as expected.
    my_third_string = "x += x + y"
    identify_operations(my_third_string)


if __name__ == "__main__":
    main()
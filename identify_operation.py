# assume that the function is split and each line of code is
# stored in a string inside a list, we loop
# so list[index] refers to each line in the string
# precondition : there is a white space around operators
def identify_operations(split_string):
    index = 0
    while index < len(split_string):
        if "+=" in split_string[index]:
            parts = split_string[index].split()
            addition_position = parts.index("+=")
            operand = parts[addition_position - 1]
            addition_value = parts[addition_position + 1]
            print("Increase {} by {}.".format(operand, addition_value))
        elif "+" in split_string[index]:
            parts = split_string[index].split()
            addition_position = parts.index("+")
            first_operand = parts[addition_position - 1]
            second_operand = parts[addition_position + 1]
            print("Add {} with {}".format(first_operand, second_operand))
        elif "-=" in split_string[index]:
            parts = split_string[index].split()
            subtraction_position = parts.index("-=")
            operand = parts[subtraction_position - 1]
            subtraction_value = parts[subtraction_position + 1]
            print("Decrease {} by {}.".format(operand, subtraction_value))
        elif "-" in split_string[index]:
            parts = split_string[index].split()
            subtraction_position = parts.index("-")
            first_operand = parts[subtraction_position - 1]
            second_operand = parts[subtraction_position + 1]
            print("Subtract {} from {}.".format(second_operand, first_operand))
        elif "**=" in split_string[index]:
            # we should do this first otherwise we're not getting into this block
            parts = split_string[index].split()
            multiply_position = parts.index("**=")
            first_operand = parts[multiply_position - 1]
            second_operand = parts[multiply_position + 1]
            print("Set {} to itself raised to the power of {}.".format(first_operand, second_operand))
        elif "**" in split_string[index]:
            parts = split_string[index].split()
            multiply_position = parts.index("**")
            first_operand = parts[multiply_position - 1]
            second_operand = parts[multiply_position + 1]
            print("Raise {} to the power of {}.".format(first_operand, second_operand))
        elif "*=" in split_string[index]:
            # *= and * are translated the same
            parts = split_string[index].split()
            multiply_position = parts.index("*=")
            first_operand = parts[multiply_position - 1]
            second_operand = parts[multiply_position + 1]
            print("Multiply {} by {}.".format(first_operand, second_operand))
        elif "*" in split_string[index]:
            # *= and * are translated the same
            parts = split_string[index].split()
            multiply_position = parts.index("*")
            first_operand = parts[multiply_position - 1]
            second_operand = parts[multiply_position + 1]
            print("Multiply {} with {}.".format(first_operand, second_operand))
        elif "//" in split_string[index]:
            #ordering matters cause if we put / before this, we never get to // block
            parts = split_string[index].split()
            int_division_position = parts.index("//")
            first_operand = parts[int_division_position - 1]
            second_operand = parts[int_division_position + 1]
            print("Divide {} by {}, rounding down to the nearest whole number.".format(first_operand, second_operand))
        elif "/=" in split_string[index]:
            parts = split_string[index].split()
            division_position = parts.index("/=")
            first_operand = parts[division_position - 1]
            second_operand = parts[division_position + 1]
            print("Divide {} by {}.".format(first_operand, second_operand))
        elif "/" in split_string[index]:
            parts = split_string[index].split()
            division_position = parts.index("/")
            first_operand = parts[division_position - 1]
            second_operand = parts[division_position + 1]
            print("Divide {} with {}.".format(first_operand, second_operand))
        elif "%=" in split_string[index]:
            parts = split_string[index].split()
            remainder_position = parts.index("%=")
            first_operand = parts[remainder_position - 1]
            second_operand = parts[remainder_position + 1]
            print("Set {} to the remainder when divided by {}.".format(first_operand, second_operand))
        elif "%" in split_string[index]:
            parts = split_string[index].split()
            modulo_position = parts.index("%")
            first_operand = parts[modulo_position - 1]
            second_operand = parts[modulo_position + 1]
            print("Find the remainder when {} is divided by {}.".format(first_operand, second_operand))
        index += 1

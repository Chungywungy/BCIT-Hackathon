import identify_operation
import identify_assignment


def parse_logical_operators(split_string, operator):
    parts = split_string.split()
    logical_operator_location = parts.index(operator)
    index = 0
    first_term = []
    parts_copy = parts[:]
    while index <= logical_operator_location:
        if parts_copy[index] == operator:
            parts.pop(0)
            index += 1
        else:
            first_term.append(parts_copy[index])
            parts.pop(0)
            index += 1
    first_operand = " ".join(first_term)
    second_operand = " ".join(parts)
    return [first_operand, second_operand]


def identify_logical_operators(split_string: str):
    if "==" in split_string:
        result = parse_logical_operators(split_string, "==")
        return "{} is equal to {}".format(result[0], identify_logical_operators(result[1]))
    elif "!=" in split_string:
        result = parse_logical_operators(split_string, "!=")
        return "{} is not equal to {}".format(result[0], identify_logical_operators(result[1]))
    elif "<=" in split_string:
        result = parse_logical_operators(split_string, "<=")
        return "{} is less than or equal to {}".format(result[0], identify_logical_operators(result[1]))
    elif ">=" in split_string:
        result = parse_logical_operators(split_string, ">=")
        return "{} is greater than or equal to {}".format(result[0], identify_logical_operators(result[1]))
    elif "<" in split_string:
        result = parse_logical_operators(split_string, "<")
        return "{} is less than {}".format(result[0], identify_logical_operators(result[1]))
    elif ">" in split_string:
        result = parse_logical_operators(split_string, ">")
        return "{} is greater than {}".format(result[0], identify_logical_operators(result[1]))
    elif "=" in split_string:
        if identify_assignment.identify_assignment(split_string):
            return identify_assignment.print_assignment(split_string)
    else:
        return identify_operation.identify_operations(split_string)


def identify_membership_operators(split_string):
    parts = split_string.split()
    if "not" in parts:
        not_index = parts.index("not")
        result = parse_logical_operators(split_string, "not")
        first_operand = identify_membership_operators(result[0])
        second_operand = identify_membership_operators(result[1])
        if parts[not_index + 1] == "in":
            if result[0] is None:
                return "is not in {}".format(second_operand)
            elif result[1] is None:
                return "{} is not in".format(first_operand)
            else:
                return "{} is not {}".format(first_operand, second_operand)
        elif parts[not_index - 1] == "is":
            if result[0] is None:
                return "not {}".format(second_operand)
            elif result[1] is None:
                return "{} not".format(first_operand)
            else:
                return "{} not {}".format(first_operand, second_operand)
        else:
            if result[0] is None:
                return "is not {}".format(second_operand)
            elif result[1] is None:
                return "{} is not".format(first_operand)
            else:
                return "{} is not {}".format(first_operand, second_operand)
    elif "and" in parts:
        result = parse_logical_operators(split_string, "and")
        first_operand = identify_membership_operators(result[0])
        second_operand = identify_membership_operators(result[1])
        if result[0] is None:
            return "and {}".format(second_operand)
        elif result[1] is None:
            return "{} and".format(first_operand)
        else:
            return "{} and {}".format(first_operand, second_operand)
    elif "or" in parts:
        result = parse_logical_operators(split_string, "or")
        first_operand = identify_membership_operators(result[0])
        second_operand = identify_membership_operators(result[1])
        if result[0] is None:
            return "or {}".format(second_operand)
        elif result[1] is None:
            return "{} or".format(first_operand)
        else:
            return "{} or {}".format(first_operand, second_operand)
    elif "is" in parts:
        result = parse_logical_operators(split_string, "is")
        first_operand = identify_membership_operators(result[0])
        second_operand = identify_membership_operators(result[1])
        if result[0] is None:
            return "is {}".format(second_operand)
        elif result[1] is None:
            return "{} is".format(first_operand)
        else:
            return "{} is {}".format(first_operand, second_operand)
    elif "in" in parts:
        result = parse_logical_operators(split_string, "in")
        first_operand = identify_membership_operators(result[0])
        second_operand = identify_membership_operators(result[1])
        if result[0] is None:
            return "in {}".format(second_operand)
        elif result[1] is None:
            return "{} in".format(first_operand)
        else:
            return "{} in {}".format(first_operand, second_operand)
    else:
        return identify_logical_operators(split_string)



def main():
    print(identify_membership_operators("x not in y"))
    print(identify_membership_operators("x not y"))
    print(identify_membership_operators("x in y"))
    print(identify_membership_operators("x in y and x is not z"))
    print(identify_logical_operators("x == y"))
    print(identify_logical_operators("x != y"))
    print(identify_logical_operators("x <= y"))
    print(identify_logical_operators("x >= y"))
    print(identify_logical_operators("x = y"))
    print(identify_logical_operators("x + y"))
    print(identify_logical_operators("x == y + z * 3"))
    print(identify_logical_operators("x > y"))
    print(identify_logical_operators("x < y"))


if __name__ == "__main__":
    main()
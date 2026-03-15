"""
This module identifies and explains logical operations and comparison operations in
a line of a function.
"""
import identify_operation
import identify_assignment


def parse_logical_operators(split_string: str, operator: str) -> list:
    """
    Divide a string by the operator in the string.

    :param split_string: string representing a line of code
    :param operator: is a logical or a membership operator
    :postcondition: convert the split_string into a list
    :postcondition: make a copy of this list
    :postcondition: find the location of the operator
    :postcondition: pop the elements in the copied list to form the second operand
    :postcondition: move each popped element into a new list to form the right operand
    :return: list containing right operands and left operands
    """
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


def identify_comparison_operators(split_string: str):
    """
    Recursively identify and explain the comparison operators in an expression in a plain English( a line of code).

    :param split_string: string representing a line of code
    :precondition: split_string is a correctly formatted string
    :postcondition: find the comparison operator and pride English description of the comparison,
                    assignment, or arithmetic operation found in split_string
    :postcondition: recursively processes split_string by splitting on the first
                    comparison operator found, formatting the left side into plain
                    English, and passing the right side back into itself until no
                    comparison operators remain; the base case delegates to
                    identify_assignment or identify_operations
    :return: a plain English string describing the full expression as a string or a call to assignment
             function if it's a simple assignment (=), or call to identify operation function to check
             for any other operations that could be in an expression
    """
    if "==" in split_string:
        result = parse_logical_operators(split_string, "==")
        return "{} is equal to {}".format(result[0], identify_comparison_operators(result[1]))
    elif "!=" in split_string:
        result = parse_logical_operators(split_string, "!=")
        return "{} is not equal to {}".format(result[0], identify_comparison_operators(result[1]))
    elif "<=" in split_string:
        result = parse_logical_operators(split_string, "<=")
        return "{} is less than or equal to {}".format(result[0], identify_comparison_operators(result[1]))
    elif ">=" in split_string:
        result = parse_logical_operators(split_string, ">=")
        return "{} is greater than or equal to {}".format(result[0], identify_comparison_operators(result[1]))
    elif "<" in split_string:
        result = parse_logical_operators(split_string, "<")
        return "{} is less than {}".format(result[0], identify_comparison_operators(result[1]))
    elif ">" in split_string:
        result = parse_logical_operators(split_string, ">")
        return "{} is greater than {}".format(result[0], identify_comparison_operators(result[1]))
    else:
        return identify_operation.identify_operations(split_string)


def identify_membership_operators(split_string: str):
    """
    Recursively identify and explain membership operations in an expression.

    Checks for operators in the order not, and, or, is, in.
    Splits the expression on the first operator found, recursively processes
    both sides, and combines them into a plain English description.
    If none of these operators are present, call
    identify_comparison_operators as the base case, which will investigate any other operations that
    might be seen in the expression such as comparison, math operations etc.

    :param split_string:  string representing a line of code
    :precondition: correctly formatted string representing a valid Python expression
    :postcondition: recursively splits split_string on the first membership or
                    logical operator found, processes the left and right sides
                    independently, and combines them into a plain English string
    :postcondition: correctly handle partial expressions where one side may be None by
                    returning only the non-None side with the other operator
    :return: a plain English string describing the full expression built
             recursively, or call to comparison operators function to check for any other
             operations in the expressions from there
    """
    parts = split_string.split()
    if "not" in parts:
        not_index = parts.index("not")
        result = parse_logical_operators(split_string, "not")
        first_operand = identify_membership_operators(result[0])
        second_operand = identify_membership_operators(result[1])
        if parts[not_index + 1] == "in":
            if result[0] is None:
                return "is not in{}".format(second_operand)
            elif result[1] is None:
                return "{}is not in".format(first_operand)
            else:
                return "{} is not{}".format(first_operand, second_operand)
        elif parts[not_index - 1] == "is":
            if result[0] is None:
                return "not {}".format(second_operand)
            elif result[1] is None:
                return "{} not".format(first_operand)
            else:
                return "{}not {}".format(first_operand, second_operand)
        else:
            if result[0] is None:
                return "is not{}".format(second_operand)
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
        return identify_comparison_operators(split_string)


def main():
    """
    Drive the program.
    """
    print(identify_membership_operators("x not in y"))
    print(identify_membership_operators("x not y"))
    print(identify_membership_operators("x in y"))
    print(identify_membership_operators("x in y and x is not z or is x and not p"))
    print(identify_comparison_operators("x == y"))
    print(identify_comparison_operators("x != y"))
    print(identify_comparison_operators("x <= y"))
    print(identify_comparison_operators("x >= y"))
    print(identify_comparison_operators("x = y"))
    print(identify_comparison_operators("x + y"))
    print(identify_comparison_operators("x == y + z * 3"))
    print(identify_comparison_operators("x > y"))
    print(identify_comparison_operators("x < y"))
    print(identify_comparison_operators("x = y"))


if __name__ == "__main__":
    main()
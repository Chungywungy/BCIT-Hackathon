# assume that the function is split and each line of code is
# stored in a string inside a list, we loop
# so list[index] refers to each line in the string
# precondition : there is a white space around operators -saba

# i think += and -= should be in assignment instead of operators, im not going to move them this instant but
# this should be considered for making everything mesh in the future when we're refactoring this -ollie

def return_operations(split_string: str, operator: str) -> list:
    """
    Extracts the two operands surrounding a given operator in a tokenized expression string.

    :param split_string: a whitespace-separated expression string
    :param operator: the operator token to locate
    :precondition: there is a white space around the operators
    :postcondition: find the index of the operator, split the strings in 2 parts,
                    first operand (left of the operator) and second operand (right of the operator)
    :return: a two-element list, the first operand (immediately left
             of the operator) and the second operand (all remaining tokens joined).
    """
    parts = split_string.split(operator)
    first_operand = parts[0].strip()
    second_operand = parts[1].strip()

    return [first_operand, second_operand]

def identify_operations(split_string: str) -> str:
    """
    Recursively translates a Python arithmetic expression string into plain English.

    :param split_string: a whitespace-separated arithmetic expression
    :precondition: split_string is a whitespace-separated expression string containing
                  at most one operator per recursive level. Compound operators ( += or -= etc.)
                  must be checked before their substrings (e.g. +) to avoid mismatches.
    :postcondition: whenever there is an operation in the line, split it calling the return_operation
                   function, to get the right hand side and left hand side of the operation
    :postcondition: repeat the process until there's no other arithmetic operation in the line
    :postcondition: if split_string contains no recognized operator, it is returned unchanged
                    as the base case of the recursion
    :return: a plain-English translation of the arithmetic operation in an expression in string
    """
    if "+=" in split_string:
        result = return_operations(split_string, "+=")

        return f"Increases {result[0]} by {identify_operations(result[1])}"
    elif "-=" in split_string:
        result = return_operations(split_string, "-=")

        return f"Decrease {result[0]} by {identify_operations(result[1])}"
    elif "**=" in split_string:
        # we should do this first otherwise we're not getting into this block
        result = return_operations(split_string, "**=")

        return f"Set {result[0]} to itself raised to the power of {identify_operations(result[1])}."
    elif "*=" in split_string:
        # *= and * are translated the same
        result = return_operations(split_string, "*=")

        return f"Multiply {result[0]} by {identify_operations(result[1])}"
    elif "/=" in split_string:
        result = return_operations(split_string, "/=")

        return f"Divide {result[0]} by {identify_operations(result[1])}"
    elif "%=" in split_string:
        result = return_operations(split_string, "%=")

        return f"Set {result[0]} to the remainder when divided by {identify_operations(result[1])}"
    elif "=" in split_string:
        result = return_operations(split_string, "=")

        return f"sets {result[0]} equal to {identify_operations(result[1])}"
    elif "**" in split_string:
        return split_string.replace("**", "^")
    else:
        return split_string


def main():
    my_string = "x += y"
    print(identify_operations(my_string))
    my_second_string = "x + y"
    print(identify_operations(my_second_string))
    # i minorly refactored this function for this exact case. i feel like this reads a heck of a lot better than
    # "increases x by x added to y" which is what the recursive case would give us. i will look more into what
    # sort of edge cases this approach could produce though and we'll come up with a final decision tmrw
    my_third_string = "x += (x + (c ** y)) * 2"
    print(identify_operations(my_third_string))


if __name__ == "__main__":
    main()
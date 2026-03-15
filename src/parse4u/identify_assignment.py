from .identify_operation import identify_operations


def identify_assignment(split_string: str) -> bool | None:
    """
    Identify whether a line of code contains an assignment statement.

    If the provided string contains a single "=" that is not part of a
    comparison operator ("=="), the function determines that the line
    represents an assignment.

    :param split_string: A string that may contain a Python assignment statement.
    :precondition: split_string is a string containing valid Python code.
    :postcondition: returns True if "=" is found in split_string, and it is not
                    part of the equality comparison operator "==".
    :postcondition: the function returns None if no assignment operator is found.
    :return: True if the line represents an assignment statement, otherwise None.
    """
    if "=" in split_string and "==" not in split_string:
        return True
    return None


def print_assignment(split_string_line: str) -> str:
    """
    Generate a natural language description of an assignment statement.

    If the provided string contains a Python assignment, the function
    separates the variable being assigned from the value or expression
    assigned to it and returns a descriptive sentence explaining the
    assignment.

    :param split_string_line: A string that may contain a Python assignment statement.
    :precondition: split_string_line is a string containing valid Python code
                  with an assignment using "=".
    :postcondition: write a descriptive string explaining which variable
                   is assigned and what value or expression it receives.
    :postcondition: the returned string describes the assignment in the
                   format "Sets <variable> equal to <value or expression>".
    :return: a descriptive string explaining the assignment.
    """
    string_parts = split_string_line.split("=")
    assignee = string_parts[0].strip()
    string_parts.pop(0)
    index = 0
    assigner = ""
    while index < len(string_parts):
        assigner = identify_operations(string_parts[index].strip())
        index += 1

    return f"Sets {assignee} equal to {assigner}"


def main():
    """
    Drives the program.
    """
    my_string = "x = y"
    if identify_assignment(my_string):
        print_assignment(my_string)
    my_string = "x = y + z"
    if identify_assignment(my_string):
        print(print_assignment(my_string))


if __name__ == "__main__":
    main()

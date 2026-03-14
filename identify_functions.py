"""
Working on adding int(), list(), str(), type(), input()

Assume that the passed argument to identify_functions() is of the format:
num_input = int(3.3)\n
variable = function(value)\n

Assume that the passed argument can contain multi-line builtin_function calls:
num_input = int(3.3) + int(1.2)\n
Although for now the logic is not yet complete, this will print out:
    converts 3.3 to an integer and converts 1.2 to an integer and assigns it to num_input
It doesn't yet address the arithmetic portion of the code


"""

def basic_builtin_functions_parser(line):
    """

    :param line:
    :precondition:  assume there are no nested function calls
    :return:
    """
    doc_string_parts = []

    english_translation_look_up = {
        "int": lambda arg: f"convert {arg} to an integer",
        "list": lambda arg: f"convert {arg} to a list",
        "str": lambda arg: f"convert {arg} to a string",
        "input": lambda arg: f"Prompts the user to enter input with text: {arg}",
    }
    if "=" in line:
        left_hand_variable = line.split("=")[0].strip()
    else:
        # doing an operation without any assignment statement
        left_hand_variable = "result"

    for basic_function, eng_translation in english_translation_look_up.items():
        remaining = line
        while basic_function + "(" in remaining:
            # stops at the index of the first parameter passed
            start = remaining.index(basic_function + "(") + len(basic_function) + 1
            # starts looking for the closing  from the start index
            end = remaining.index(")", start)
            args = remaining[start: end].strip()
            doc_string_parts.append(eng_translation(args))
            # looks if there are any instances of other basic functions invoked in the line
            remaining = remaining[end + 1:]

    if doc_string_parts:
        return " and ".join(doc_string_parts) + f" and assigns it to {left_hand_variable}"
    return None

def main():
    sample_line = "num_input = int(3.3)\n"
    print(basic_builtin_functions_parser(sample_line))
    # converts 3.3 to an integer and assigns it to num_input

    # partial completion
    multi_line = "num_input = int(3.3) + int(1.2)\n"
    print(basic_builtin_functions_parser(multi_line))
    # converts 3.3 to an integer and converts 1.2 to an integer and assigns it to num_input

    # may not be able to handle nested function calls?
    nested = "num_input = list(int(3.3)) + int(1.2)\n"
    print(basic_builtin_functions_parser(nested))
    # converts 3.3 to an integer and converts 1.2 to an integer and assigns it to num_input

if __name__ == "__main__":
    main()



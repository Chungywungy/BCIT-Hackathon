"""
Working on adding int(), list(), str(), type(), input(), print()

Assume that the passed argument to identify_functions() is of the format:
    num_input = int(3.3)\n
    variable = function(value)\n

    input('Type in a number: ')\n
    function(value)\n

Assume that the passed argument can contain multi-line builtin_function calls:
    num_input = int(3.3) + int(1.2)\n

Although for now the logic is not yet complete, this will print out:
    converts 3.3 to an integer and converts 1.2 to an integer and assigns it to num_input

It doesn't yet address the arithmetic portion of the code:
    num_input = list(int(3.3)) + int(1.2)\n

This will run with no crashes but will print out:
    convert 3.3 to an integer and convert 1.2 to an integer and assigns it to num_input


"""
import identify_assignment
from identify_operation import return_operations


def basic_builtin_functions_parser(line):
    """

    :param line:
    :precondition:  assume there are no nested function calls
    :return:
    """
    doc_string_parts = []

    # lambda functions that will take in a single parameter argument and adds an English translation
    english_translation_look_up = {
        "int": lambda arg: f"convert {arg} to an integer",
        "list": lambda arg: f"convert {arg} to a list",
        "str": lambda arg: f"convert {arg} to a string",
        "type": lambda arg: f"gets the type of {arg}",
        "input": lambda arg: f"prompts the user to: {arg}",
        "print": lambda arg: f"prints {arg} to the console",
    }
    if "=" in line:
        left_hand_variable = line.split("=")[0].strip()
    else:
        # doing an operation without any assignment statement
        # e.g. int(3.2) -> this will omit the assigns to variable name part
        left_hand_variable = None

    for basic_function, eng_translation in english_translation_look_up.items():
        remaining = line
        while basic_function + "(" in remaining:
            function_call_index = remaining.index(basic_function + "(")
            # make sure it's not part of another word e.g. "int" inside "print"
            if function_call_index > 0 and remaining[function_call_index - 1].isalpha():
                break
            # stops at the index of the first parameter passed
            start = remaining.index(basic_function + "(") + len(basic_function) + 1
            # starts looking for the closing  from the start index
            end = remaining.index(")", start)
            # slices the line to parse argument
            args = remaining[start: end].strip()
            doc_string_parts.append(eng_translation(args))
            # looks if there are any instances of other basic functions invoked in the line
            remaining = remaining[end + 1:]

    if doc_string_parts:
        if left_hand_variable:
            return " and ".join(doc_string_parts) + f" and assigns it to {left_hand_variable}"
        return " and ".join(doc_string_parts)

    return None


def basic_builtin_functions_parser_new(line):
    my_string = identify_assignment.print_assignment(line)
    start_idx = my_string.find("to") + 2

    arguments = my_string[start_idx:].split("and")
    if len(arguments) > 1:
        for idx in range(len(arguments) - 1):
            arguments[idx] = arguments[idx].split("of")[1]

    doc_string_parts = []

    english_translation_look_up = {
        "int": lambda param: f"{param} as an integer",
        "list": lambda param: f"{param} as a list",
        "str": lambda param: f"{param} as a string",
        "type": lambda param: f"the type of {param}",
        "input": lambda param: f"prompts the user to: {param}",
        "print": lambda param: f"prints {param} to the console",
    }

    for argument in arguments:
        func_name, param = argument.split("(")
        func_name, param = func_name.strip(), param[:-1].strip().replace(")", "")

        doc_string_parts.append(english_translation_look_up[func_name](param))

    new_string = my_string
    for i in range(len(arguments)):
        new_string = new_string.replace(arguments[i].strip(), doc_string_parts[i])

    return new_string


def main():
    # # Safe Use Cases
    # # int - convert a float to an integer
    # int_line = "num_input = int(3.3)\n"
    # print(basic_builtin_functions_parser(int_line))
    # # convert 3.3 to an integer and assigns it to num_input
    #
    # int_line_no_assignment = "int(3.3)\n"
    # print(basic_builtin_functions_parser(int_line_no_assignment))
    # # convert 3.3 to an integer and assigns it to num_input
    #
    # # str - convert a number to a string
    # str_line = "str_input = str(42)\n"
    # print(basic_builtin_functions_parser(str_line))
    # # convert 42 to a string and assigns it to str_input
    #
    # # list - convert a tuple to a list
    # list_line = "list_input = list(my_tuple)\n"
    # print(basic_builtin_functions_parser(list_line))
    # # convert my_tuple to a list and assigns it to list_input
    #
    # # type - get the type of a variable
    # type_line = "type_input = type(my_var)\n"
    # print(basic_builtin_functions_parser(type_line))
    # # gets the type of my_var and assigns it to type_input
    #
    # # input - prompt the user
    # input_line = "user_input = input(Enter your name: )\n"
    # print(basic_builtin_functions_parser(input_line))
    # # prompts the user to: Enter your name:  and assigns it to user_input
    #
    # # print - no assignment
    # print_line = "print(my_var)\n"
    # print(basic_builtin_functions_parser(print_line))
    # # prints my_var to the console
    #
    # # In-progress use cases
    # print("\n\nIn-progress use cases")
    # # partial completion
    # multi_line = "num_input = int(3.3) + int(1.2)\n"
    # print(basic_builtin_functions_parser(multi_line))
    # # converts 3.3 to an integer and converts 1.2 to an integer and assigns it to num_input
    # # doesn't handle the logic for arithmetic operations yet

    # may not be able to handle nested function calls?
    # converts 3.3 to an integer and converts 1.2 to an integer and assigns it to num_input
    # doesn't handle the logic for nested basic function calls yet
    print("\n\n")

    # nested = "num_input = int(1.2)\n"
    # print(basic_builtin_functions_parser_new(nested))
    #
    # nested = "num_input = int(1.2) + int(1.2)\n"
    # print(basic_builtin_functions_parser_new(nested))
    #
    # nested = "num_input = int(1.2) + int(1.2) + int(3.3)\n"
    # print(basic_builtin_functions_parser_new(nested))

    nested = "num_input = int(1.2) + int(1.2) + int(3.3) + list(3.4)\n"
    print(basic_builtin_functions_parser_new(nested))
    print(identify_assignment.print_assignment(nested))

if __name__ == "__main__":
    main()



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

def replaces_function_calls(line):
    english_translation_look_up = {
        "int": lambda param: f"{param} as an integer",
        "list": lambda param: f"{param} as a list",
        "str": lambda param: f"{param} as a string",
        "type": lambda param: f"the type of {param}",
        "input": lambda param: f"prompts the user to: {param}",
        "print": lambda param: f"prints {param} to the console",
        "range": lambda param: f"range of {param}"
    }

    new_string = line

    for basic_function, eng_translation in english_translation_look_up.items():
        remaining = new_string
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
            function_call = remaining[function_call_index: end + 1]
            new_string = new_string.replace(function_call, eng_translation(args))
            # looks if there are any instances of other basic functions invoked in the line
            remaining = remaining[end + 1:]

    return new_string


def main():
    # nested = "num_input = int(1.2) + int(1.2) + int(3.3) + list(3.4)\n"
    # print(basic_builtin_functions_parser_new(nested))
    # print(identify_assignment.print_assignment(nested))
    iter = """for i in (range(3)):
            print(i)"""
    print(replaces_function_calls(iter))


if __name__ == "__main__":
    main()



def replaces_function_calls(line):
    """
    Acts as the final call to a function which translate any builtin function to its English counterpart. The function
    will not interfere with any of the grammatical structure of the passed string. That is, it will only replace a
    builtin named function.

    :param line:
    :return:
    """
    english_translation_look_up = {
        "int": lambda param: f"{param} as an integer",
        "list": lambda param: f"{param} as a list",
        "str": lambda param: f"{param} as a string",
        "type": lambda param: f"the type of {param}",
        "input": lambda param: f"user input provided from the prompt {param}",
        "print": lambda param: f"prints {param} to the console",
        "range": lambda param: f"range of {param}",
        "len": lambda param: f"length of {param}"
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
            end = remaining.rindex(")", start)
            # slices the line to parse argument
            args = remaining[start: end].strip()
            function_call = remaining[function_call_index: end + 1]
            new_string = new_string.replace(function_call, eng_translation(args))
            # looks if there are any instances of other basic functions invoked in the line
            remaining = remaining[end + 1:]

    return new_string


def main():
    pass


if __name__ == "__main__":
    main()



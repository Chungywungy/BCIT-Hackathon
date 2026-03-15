def replaces_function_calls(line: str) -> str:
    """
    Generate a natural language translation of built-in Python function calls.

    If the provided string contains built-in Python functions (such as int,
    str, len, print, etc.), the function replaces those calls with their
    English descriptions while preserving the rest of the sentence structure.

    :param line: A string that may contain built-in Python function calls.
    :precondition: line is a string containing valid Python code or expressions.
    :postcondition: any recognized built-in function calls in the string are
                    replaced with their English equivalents.
    :postcondition: parts of the string that do not contain recognized
                    function calls remain unchanged.
    :return: a string where built-in Python function calls are replaced with
             descriptive English phrases.
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
            try:
                # apparently the ) was sliced off in the previous iteration,
                # try except will fix this
                end = remaining.rindex(")", start)
            except ValueError:
                break
            # slices the line to parse argument
            args = remaining[start: end].strip()
            function_call = remaining[function_call_index: end + 1]
            new_string = new_string.replace(function_call, eng_translation(args))
            # looks if there are any instances of other basic functions invoked in the line
            remaining = remaining[end + 1:]

    return new_string


def main():
    """
    Drive the program.
    """
    return


if __name__ == "__main__":
    main()



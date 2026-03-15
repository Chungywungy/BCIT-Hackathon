def try_and_except(split_string: str) -> str | None:
    """
    Generate a natural language description of try, except, raise, or finally statements.

    If the provided string contains Python exception-handling keywords, the function
    translates them into descriptive English sentences explaining the program's behavior.

    :param split_string: A string that may contain Python exception-handling statements.
    :precondition: split_string is a string containing valid Python code.
    :postcondition: returns a descriptive string explaining the behavior of try,
                    raise, except, or finally statements if they are found in split_string.
    :postcondition: the function returns None if no exception-handling keywords
                    are found in split_string.
    :return: a descriptive string explaining the exception-handling behavior,
             or None if no relevant statement is present.
    """
    lines = split_string.split()

    for term in lines:
        if "try:" == term:
            return "The function tries performing the following actions:"
        elif "raise" in term:
            error = lines[1].split("(")
            error_message = error[1] + " " + lines[2].replace(")","")
            return f"The function will raise an {error[0]} with message, {error_message}."
        elif "except" in term:
            lines[1] = lines[1].replace(":", "")
            return f"If the function fails to perform these actions a {lines[1]} will occur, so the function:"
        elif "finally:" == term:
            return "Finally, the function will:"
        else:
            return None


def main():
    """
    Drive the program.
    """
    print(try_and_except("try:"))
    print(try_and_except("except ValueError:"))
    print(try_and_except("raise ValueError(\"Useful message\")"))
    print(try_and_except("finally:"))

if __name__ == "__main__":
    main()
from .parse_function_declaration import parse_function_declaration
from .iterables import conditionals


def generate(width: int=0) -> str:
    """
    Generate a natural language description of a user-provided Python function.

    The function reads lines of Python code from user input until "END" is
    entered or an EOF signal is received. It then parses the function
    declaration and the remaining lines to produce a descriptive summary
    of the function's behavior.

    :param: a syntactically correct Python function
    :precondition: the user provides lines of valid Python function code
                   followed by "END" or an EOF signal.
    :postcondition: print a natural language description of the function
                    declaration and its internal logic.
    :return: a string containing the generated natural language description
             of the function body.
    """
    print("Enter/Paste non-built-in Python function code. Type \" END \" or press Ctrl-D to save it.")
    contents = []
    while True:
        try:
            line = input()
            if line == "END":
                break
        except EOFError:
            break
        contents.append(line)

    line1 = parse_function_declaration(contents[0])
    contents.pop(0)
    result = conditionals(contents)

    if width:
        result = format_text(result, width)

    print(line1)
    print(result)

def format_text(text: str, width: int=150):
    words = text.split()  # splits on any whitespace
    lines = []
    current = ""

    for word in words:
        candidate = current + " " + word if current else word
        if len(candidate) <= width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word

    if current:
        lines.append(current)

    return "\n".join(lines)


def main():
    """
    Drive the program.
    """
    generate()
    return


if __name__ == "__main__":
    main()

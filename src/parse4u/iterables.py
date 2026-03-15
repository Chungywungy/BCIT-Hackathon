from .identify_logical_operators import identify_comparison_operators
from .identify_functions import replaces_function_calls
from .try_except import try_and_except


def while_loop(split_string: str) -> str | None:
    """
    Generate a natural language description of a while loop.

    If the provided string contains a Python while statement, the function
    extracts the loop condition and returns a descriptive sentence explaining
    the loop's behavior.

    :param split_string: A string that may contain a Python while loop.
    :precondition: split_string is a string containing valid Python code.
    :postcondition: write a descriptive string explaining the loop condition and behavior
                    If "while" is found in split_string.
    :postcondition: the function returns None if "while" is not found in split_string.
    :return: a descriptive string explaining the while loop, or None if no
             while loop is present.
    """
    if "while" in split_string:
        storage = split_string.split(":")[0].split("while")[1].strip()

        return (f'While {replaces_function_calls(identify_comparison_operators(storage))} is true, it repeatedly '
                f' {continuation(split_string)}{breaker(split_string)}{passer(split_string)}')
    return None


def for_loop(split_string: list[str]) -> str | None:
    """
    Generate a natural language description of a for loop.

    If the provided string contains a Python for statement, the function
    extracts the loop variable and iterable and returns a descriptive
    sentence explaining the loop's behavior.

    :param split_string: A string that may contain a Python for loop.
    :precondition: split_string is a list of strings containing valid Python code.
    :postcondition: write a descriptive string explaining the loop variable
                    and iterable if "for" is found in split_string, and it
                    represents a valid for loop.
    :postcondition: the function returns None if "for" is not found in
                    split_string or if it is part of another word.
    :return: a descriptive string explaining the for loop, or None if no
             valid for loop is present.
    """
    if "for" in split_string:
        idx = split_string.find("for")
        if split_string[idx + len("for")].isalpha(): return None
        split_string = split_string.split()
        return (
            f"Iterates through each {split_string[1]} in the {replaces_function_calls(split_string[3].replace(":", ""))}"
            f" using a for loop. "
            f"{continuation(split_string)}{breaker(split_string)}{passer(split_string)} ")
    return None


def continuation(split_string: str) -> str:
    """
    Generate a natural language description of a continue statement.

    If the provided string contains a Python continue statement, the function
    returns a sentence describing that the loop immediately restarts from
    the beginning.

    :param split_string: A string that may contain a Python continue statement.
    :precondition: split_string is a string containing valid Python code.
    :postcondition: write a descriptive string explaining that the loop
                    returns to the top and begins again if "continue"
                    is found in split_string.
    :postcondition: the function returns an empty string if "continue"
                    is not found in split_string.
    :return: a descriptive string explaining the continue behavior,
             or an empty string if no continue statement is present.
    """
    if "continue" in split_string:
        return f"the loop then goes to the top and begins again "
    return ""


def breaker(split_string: str) -> str:
    """
    Generate a natural language description of a break statement.

    If the provided string contains a Python break statement, the function
    returns a sentence describing that the loop exits.

    :param split_string: A string that may contain a Python break statement.
    :precondition: split_string is a string containing valid Python code.
    :postcondition: write a descriptive string explaining that the loop
                    exits if "break" is found in split_string.
    :postcondition: the function returns an empty string if "break"
                    is not found in split_string.
    :return: a descriptive string explaining the break behavior,
             or an empty string if no break statement is present.
    """
    if "break" in split_string:
        return f"it then exits the loop "
    else:
        return ""


def passer(split_string: str) -> str:
    """
    Generate a natural language description of a pass statement.

    If the provided string contains a Python pass statement, the function
    returns a sentence describing that the pass statement is executed.

    :param split_string: A string that may contain a Python pass statement.
    :precondition: split_string is a string containing valid Python code.
    :postcondition: write a descriptive string explaining that pass is called
                    if "pass" is found in split_string.
    :postcondition: the function returns an empty string if "pass"
                    is not found in split_string.
    :return: a descriptive string explaining the pass behavior,
             or an empty string if no pass statement is present.
    """
    if "pass" in split_string:
        return "calls pass"
    else:
        return ""


def conditionals(split_string: list) -> str:
    """
    Generate a natural language description of conditional and loop statements.

    If the provided list contains Python conditional statements (if, elif, else)
    or loop/control statements, the function parses each line and converts it
    into a descriptive sentence explaining the program's behavior.

    :param split_string: A list of strings representing lines of Python code.
    :precondition: split_string is a list containing strings of valid Python code.
    :postcondition: write descriptive strings explaining conditional statements,
                    loops, and control flow if they are found in split_string.
    :postcondition: lines are returned as processed natural language descriptions as a string.
    :return: a single string containing the combined natural language description of the provided code.
    """
    lambdamentality = {
        "if": lambda statement: f"checks if {replaces_function_calls(identify_comparison_operators(statement))} then ",
        "elif": lambda
            statement: f"otherwise it checks {replaces_function_calls(identify_comparison_operators(statement))} then ",
        "else": lambda statement: f"otherwise it will "
    }

    container = []

    for line in split_string:
        non_applicable = False
        for cond in {"elif", "else", "if"}:
            if cond in line:
                argument = line[len(cond):].strip().split(":")[0]
                container.append(f"{lambdamentality[cond](argument)}")
                non_applicable = True
                break

            while_output = while_loop(line)
            if while_output:
                container.append(while_output)
                non_applicable = True
                break

            for_output = for_loop(line)
            if for_output:
                container.append(for_output)
                non_applicable = True
                break

            continuation_output = continuation(line)
            if continuation_output:
                container.append(continuation_output + "\n")
                non_applicable = True
                break

            breaker_output = breaker(line)
            if breaker_output:
                container.append(breaker_output + "\n")
                non_applicable = True
                break

            passer_output = passer(line)
            if passer_output:
                container.append(passer_output + "\n")
                non_applicable = True
                break

            try_except_output = try_and_except(line)
            if try_except_output:
                container.append(try_except_output + "\n")
                non_applicable = True
                break

        if not non_applicable:
            value = replaces_function_calls(identify_comparison_operators(line))
            container.append(value.strip() + "\n")

    return "".join(container)


def main():
    """
    Drive the program.
    """
    code_block_conditionals = ["if 1 > int(2):", "do_anything()", "elif 1 < range(2):", "please_work()", "else:",
                               "1 + 2"]
    sample = ["while number > 1: pass"]
    return conditionals(sample)


if __name__ == "__main__":
    print(main())

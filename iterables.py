from identify_operation import *
from identify_logical_operators import *
from identify_functions import *

def while_loop(split_string: str) -> str | None:
    if "while" in split_string:
        storage = split_string.split(":")[0].split("while")[1].strip()


        return f'While {replaces_function_calls(identify_comparison_operators(storage))} is true, it repeatedly executes {continuation(split_string)}'


def for_loop(split_string: str) -> str | None:
    if "for" in split_string:
        split_string = split_string.split()
        return f"Iterates through each {split_string[1]} in the {replaces_function_calls(split_string[3].replace(":", ""))} using a for loop. {continuation(split_string)} "


def continuation(split_string):
    if "continue" in split_string:
        return f"the loop then goes to the top and begins again"
    else:
        return ""


def conditionals(split_string: list):
    lambdamentality = {
        "if": lambda statement: f"checks {replaces_function_calls(identify_comparison_operators(statement))} then ",
        "elif": lambda statement: f"otherwise it checks {replaces_function_calls(identify_comparison_operators(statement))} then ",
        "else": lambda statement: f"if none of these conditions are true it executes "
    }

    container = []

    for line in split_string:
        non_applicable = False
        for cond in {"elif", "else", "if"}:
            if cond in line:
                argument = line[len(cond):].strip().split(":")[0]
                container.append(f"{lambdamentality[cond](argument)}" )
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

        if not non_applicable:
            value = replaces_function_calls(identify_comparison_operators(line))
            container.append(value.strip()+"\n")


    return "".join(container)


def main():
    code_block_conditionals = ["if 1 > int(2):", "do_anything()", "elif 1 < range(2):", "please_work()", "else:", "1 + 2"]
    sample = ["while number > 1: continue "]
    return conditionals(sample)

if __name__ == "__main__":
    print(main())
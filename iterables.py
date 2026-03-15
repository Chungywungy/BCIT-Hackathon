from identify_operation import *
from identify_logical_operators import *
from identify_functions import *

def while_loop(split_string):
    if "while" in split_string:
        storage = []
        cache = []
        colon_checker = False
        for letter in split_string:
            if letter != ":":
                storage.append(letter)
            else:
                break

        storage = "".join(storage)
        for letter in split_string:
            if colon_checker:
                cache.append(letter)
            if letter == ":":
                colon_checker = True


        cache = "".join(cache)


        return f'{identify_comparison_operators(storage)} is true, it repeatedly executes'f' {identify_operations(cache)}.'


def for_loop(split_string):
    if "for" in split_string:
        split_string = split_string.split()
        return f"Iterates through each {split_string[1]} in the {split_string[3].replace(":", "")} using a for loop."

def conditionals(split_string: list):
    lambdamentality = {
        "if": lambda statement: f"checks {replaces_function_calls(identify_comparison_operators(statement))} then ",
        "elif": lambda statement: f"otherwise it checks {replaces_function_calls(identify_comparison_operators(statement))} then ",
        "else": lambda statement: f"if none of these conditions are true it gets "
    }

    container = []

    for line in split_string:
        contains_cond = False
        for cond in {"elif", "else", "if"}:
            if cond in line:
                argument = line[len(cond):].strip().split(":")[0]
                container.append(f"{lambdamentality[cond](argument)}" )
                contains_cond = True
                break

            while_output = while_loop(line)
            if while_output:
                container.append(while_output)
                break
            for_output = for_loop(line)
            if for_output:
                container.append(for_output)
                break
        if not contains_cond:
            value = replaces_function_calls(identify_comparison_operators(line))
            container.append(value.strip()+"\n")


    return "".join(container)


def main():
    code_block_while_loop = "while alakazam > 1: \n  abra + cadabra"
    code_block_for_loop = "for abra in cadabra: \n  do_something()"
    code_block_conditionals = ["if 1 > int(2):", "do_anything()", "elif 1 < range(2):", "please_work()", "else:", "1 + 2"]
    return conditionals(code_block_conditionals)

if __name__ == "__main__":
    print(main())
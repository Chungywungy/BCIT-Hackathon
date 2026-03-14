from identify_operation import *
from identify_logical_operators import *


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


        print(f'{identify_logical_operators(storage)} is true, it repeatedly executes'f' {identify_operations(cache)}.')
    return


def for_loop(split_string):
    if "for" in split_string:
        split_string = split_string.split()
        print(f"Iterates through each {split_string[1]} in the {split_string[3].replace(":", "")} using a for loop.")
    return

def conditionals(split_string):
    if "if" in split_string:
        storage = []
        for letter in split_string:
            if letter != ":":
                storage.append(letter)
            else:
                break
        storage = "".join(storage)

    print(f"checks {identify_logical_operators(storage)}")

    if "elif" in split_string:
        colon_checker = True
        value = 'elif'
        elif_checker = split_string.index(value)
        elif_storage = []

        big_list = split_string[elif_checker + 2:]
        for letter in big_list:
            if colon_checker:
                elif_storage.append(letter)
            if letter == ":":
                colon_checker = False

        elif_storage = "".join(elif_storage[:-1])

    print(f"otherwise it checks {identify_logical_operators(elif_storage)}")

    if "else" in split_string:
        colon_checker = False
        value = 'else'
        else_checker = split_string.index(value)
        else_storage = []

        big_list = split_string[else_checker + 2:]
        for letter in big_list:
            if colon_checker:
                else_storage.append(letter)
            if letter == ":":
                colon_checker = True

    else_storage = "".join(else_storage)

    print(f"otherwise it checks {identify_logical_operators(else_storage)}")
    return


def main():
    code_block_while_loop = "while alakazam > 1: \n  abra + cadabra"
    code_block_for_loop = "for abra in cadabra: \n  do_something()"
    code_block_conditionals = "if 1 > 2: \n do_anything() \n elif 1 < 2: please_work() \n else: 1 + 2"
    return while_loop(code_block_while_loop), for_loop(code_block_for_loop), conditionals(code_block_conditionals)


if __name__ == "__main__":
    main()
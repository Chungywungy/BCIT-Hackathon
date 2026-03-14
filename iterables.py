from identify_operation import *
from identify_logical_operators import *


def while_loop(split_string):
    if "while" in split_string:
        storage = []
        test = []
        colon_checker = False
        for letter in split_string:
            if letter != ":":
                storage.append(letter)
            else:
                break

        storage = "".join(storage)
        for letter in split_string:
            if colon_checker:
                test.append(letter)
            if letter == ":":
                colon_checker = True


        test = "".join(test)


        print(f'{identify_logical_operators(storage)} is true, it repeatedly executes'f' {identify_operations(test)}.')
    return


def for_loop(split_string):
    if "for" in split_string:
        split_string = split_string.split()
        print(f"Iterates through each {split_string[1]} in the {split_string[3].replace(":", "")} using a for loop.")
    return


def main():
    code_block_while_loop = "while alakazam > 1: \n  abra + cadabra"
    code_block_for_loop = "for abra in cadabra: \n  do_something()"
    return while_loop(code_block_while_loop), for_loop(code_block_for_loop)


if __name__ == "__main__":
    main()
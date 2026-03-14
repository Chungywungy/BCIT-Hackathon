def while_loop(split_string):
    if "while" in split_string:
        split_string = split_string.split()
        print(f'Repeatedly executes while {split_string[1].replace(":", "")} is true.')
    return


def for_loop(split_string):
    if "for" in split_string:
        split_string = split_string.split()
        print(f"Iterates through each {split_string[1]} in the {split_string[3].replace(":", "")} using a for loop.")
    return


def main():
    code_block_while_loop = "while alakazam: \n  do_something()"
    code_block_for_loop = "for abra in cadabra: \n  do_something()"
    return while_loop(code_block_while_loop), for_loop(code_block_for_loop)


if __name__ == "__main__":
    main()
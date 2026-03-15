import identify_operation


def identify_assignment(split_string: str):
    if "=" in split_string and "==" not in split_string:
        return True
    return None


def print_assignment(split_string_line: str):
    string_parts = split_string_line.split("=")
    assignee = string_parts[0].strip()
    string_parts.pop(0)
    index = 0
    assigner = ""
    while index < len(string_parts):
        assigner = identify_operation.identify_operations(string_parts[index].strip())
        index += 1

    return f"Sets {assignee} equal to {assigner}"


def main():
    my_string = "x = y"
    if identify_assignment(my_string):
        print_assignment(my_string)
    my_string = "x = y + z"
    if identify_assignment(my_string):
        print(print_assignment(my_string))


if __name__ == "__main__":
    main()

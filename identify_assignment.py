import identify_operation


def identify_assignment(split_string: list):
    for line in split_string:
        if "=" in line and "==" not in line:
            print_assignment(line)

def print_assignment(split_string_line: str):
    string_parts = split_string_line.split("=")
    assignee = string_parts[0]
    index = 1

    assigner = identify_operation.identify_operations(string_parts)
    print(f"Sets {assignee} equal to {assigner}")


def main():
    my_string = "def my_function(x, y): \n x = y"
    my_split_string = my_string.split("\n")
    identify_assignment(my_split_string)


if __name__ == "__main__":
    main()

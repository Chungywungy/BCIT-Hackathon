import parse_function_declaration
import iterables


def main():
    print("Enter/Paste your content. Type \" END \" or press Ctrl-D or Ctrl-Z on windows to save it.")
    contents = []
    while True:
        try:
            line = input()
            if line == "END":
                break
        except EOFError:
            break
        contents.append(line)


    line1 = parse_function_declaration.parse_function_declaration(contents[0])
    contents.pop(0)
    result = iterables.conditionals(contents)

    print(line1)
    print(result)

if __name__ == "__main__":
    main()
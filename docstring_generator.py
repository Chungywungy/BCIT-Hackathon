import parse_function_declaration
import identify_logical_operators

def main():
    print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.")
    contents = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        contents.append(line)

    line1 = parse_function_declaration.parse_function_declaration(contents[0])
    for line in contents:
        pass
        #id iterables
        #which should id functions
        #which should id membership operations
        #which should id logic operations
        #you get the idea
        #then store it in a list and go through the list printing line by line.

    print(line1)

if __name__ == "__main__":
    main()
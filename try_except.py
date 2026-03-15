import parse_function_declaration
import iterables

def try_and_except(split_string):
    lines = split_string.split()

    for term in lines:
        if "try:" == term:
            return "The function tries performing the following actions:"
        elif "raise" in term:
            error = lines[1].split("(")
            error_message = error[1] + " " + lines[2].replace(")","")
            return f"The function will raise an {error[0]} with message, {error_message}."
        elif "except" in term:
            lines[1] = lines[1].replace(":", "")
            return f"If the function fails to perform these actions a {lines[1]} will occur, so the function will:"
        elif "finally:" == term:
            return "Finally, the function will:"
        else:
            return None


def main():
    print(try_and_except("try:"))
    print(try_and_except("except ValueError:"))
    print(try_and_except("raise ValueError(\"Useful message\")"))
    print(try_and_except("finally:"))

if __name__ == "__main__":
    main()
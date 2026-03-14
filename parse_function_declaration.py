"""
Parses functions declarations and annotations.

Assumption: 
Only parses annotations when available

def function_name(x: int, y: float) -> int:
def function_name(x, y):
def function_name() -> str:
def function_name():
"""


def get_return_type(function_string):
    """
    Get return type.
    :param function_string:
    :return:
    """
    if "def" and "->" in function_string:
        return_type = function_string.split("->")
        return_type = return_type[1].replace(":", "").strip()
        # this gets the return type of the function
    else:
        return_type = None  # return type is None when the function_string does not include the return annotation
    # print("return type:", return_type)
    return return_type


def get_function_name(function_string):
    """
    Get function name.
    :param function_string:
    :return:
    """
    # removes def from the string
    if "def" in function_string:
        function_string = function_string.replace("def", "")

    split_function_string = function_string.split("(")
    function_name = split_function_string[0].strip()
    # splits string at ( to get the function name
    # print("function name:", function_name)

    return function_name


def get_parameters(function_string):
    """
    Get parameters in function.
    :param function_string:
    :return:
    """
    left_split_function_string = function_string.split("(")

    right_split_function_string = left_split_function_string[1].split(")")
    parameters = right_split_function_string[0]
    # split at the '(' and ')' to get everything in between the parentheses

    if parameters and ":" in parameters:  # runs if there are parameters with annotations
        parameters_list = parameters.split(",")  # returns a list of variables and function annotations

        # parse parameters; create dictionary to hold each parameter and its type
        variable_type_dict = {}
        for item in parameters_list:
            stripped_item = item.strip()

            if ":" in stripped_item:
                parameter_annotation = stripped_item.split(":")
                variable = parameter_annotation[0].strip()  # this gets the variable that will become the key in dict
                variable_type = parameter_annotation[1].strip()  # this is the variable type that will be the value pair
                variable_type_dict[variable] = variable_type

        # iterating through the variables to create a list to hold parameter descriptions
        parameter_description = []
        for key, value in variable_type_dict.items():
            parameter_description.append(f"{key} as {value}")
        # creates list to hold parameter descriptions i.e. ['x as int, y as float']

        parameter_text = ", ".join(parameter_description)  # turn the parameter list into a one line string

    elif parameters and ":" not in parameters:  # runs case where parameters exist, but no annotations are written
        parameters_list = parameters.split(",")
        stripped_parameters_list = []

        for item in parameters_list:
            stripped_item = item.strip()
            stripped_parameters_list.append(stripped_item)
        parameter_text = ", ".join(stripped_parameters_list)  # creates list to hold parameters

    else:
        parameter_text = "no parameters"

    return parameter_text


def parse_function_declaration(function_string):
    """
    Put together full text string to parse function.
    :param function_string:
    :return:
    """
    return_type = get_return_type(function_string)
    function_name = get_function_name(function_string)
    parameter_text = get_parameters(function_string)

    if return_type:  # runs if there is a return type (not None)
        function_declaration_string = (f"{function_name} is declared as a function. It takes {parameter_text} and "
                                       f"returns {return_type}.")
    else:  #runs if there return type is None
        function_declaration_string = f"{function_name} is declared as a function. It takes {parameter_text}."

    return function_declaration_string


def main():
    """
    Drive the function.
    """
    # with parameters and annotations
    parse_function_declaration("def function_name(x: int, y: float, z: str) -> int:")

    # with parameters without annotations
    parse_function_declaration("def function_name(x, y) -> int:")

    # with parameters without annotations, without return annotation
    parse_function_declaration("def function_name(x, y)")

    #without parameters
    parse_function_declaration("def another_function() -> int:")

    #without parameters and return annotation
    parse_function_declaration("def wow_another_one():")


if __name__ == "__main__":
    main()


"""
Assumption: 
functions must be annotated with variable and return type. 

def function_name(x: int, y: float) -> int:
"""
def parse_function_declaration(function_string):
    # get the function name
    if "def" in function_string:
        function_string = function_string.replace("def", "")

        #split return type value
        if "->" in function_string:
            return_type = function_string.split("->")
            return_type = return_type[1].replace(":", "").strip()
            # print(f"return type: {return_type}")

        function_string = function_string.split("(")
        function_name = function_string[0].strip()
        # print(f"{function_name} is declared as a function")

    #get parameters
    function_string = function_string[1]
    parameters = function_string.split("->")
    parameters = parameters[0]
    parameters = parameters.replace(")", "")
    # print("parameters:", parameters)

    if parameters:
        parameters_list = parameters.split(",") # returns a list of variables and function annotations
        # print("parameters:", parameters_list)

        #parse parameters
        variable_type_dict = {}
        for item in parameters_list:
            item.strip()
            
            if ":" in item:
                variable_type = item.split(":")
                # print(f"variable_type: {variable_type}")
                variable = variable_type[0].strip()
                type = variable_type[1].strip()
                variable_type_dict[variable] = type
                # print(variable_type_dict)

        # iterating through the variables to create a list to hold parameter descriptions
        parameter_description = []
        for key, value in variable_type_dict.items():
            parameter_description.append(f"{key} as {value}")
        # print(parameter_description)

    if parameters == "":
        parameter_text = "no parameters"
    else:
        parameter_text = ", ".join(parameter_description)

    function_declaration_string = f"{function_name} is declared as a function. It takes {parameter_text} and returns {return_type}."
    # print(function_declaration_string)
    
    return function_declaration_string


def main():
    parse_function_declaration("def function_name(x: int, y: float) -> int:")



if __name__ == "__main__":
    main()

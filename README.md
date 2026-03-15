# BCIT-Hackathon

# About
This program allows users to input non-built-in Python functions and receive a plain-English explanation of
what the function does. The system analyzes the structure and logic of the code, then translates it into a concise
summary that is easy for beginner developers to understand. The goal is to make learning programming easier by
helping users quickly grasp how code works without needing more advanced knowledge.


# Instructions
1. Open terminal
2. type in "pip install parse4u"
```terminaloutput
$ python -m pip install parse4u
```
3. open python file
4. import parse4u
5. type in "generate()"
```python
from parse4u import *

generate()
```
6. Enter (or copy and paste) your code for your Python function
7. Press Ctrl + D or type "END" to start parsing your code

```terminaloutput
Enter/Paste your content. Type " END " or press Ctrl-D or Ctrl-Z on windows to save it.

def something():
    return nothing
END

OUTPUT:
something is declared as a function. It takes no parameters.
return nothing
```

# Authors
Placeholder

# License
This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
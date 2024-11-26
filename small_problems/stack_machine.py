"""
n: Place an integer value, n, in the register. Do not modify the stack.
PUSH : Push the current register value onto the stack. Leave the value in the register.
ADD : Pop a value from the stack and add it to the register value, storing the result in the register.
SUB : Pop a value from the stack and subtract it from the register value, storing the result in the register.
MULT : Pop a value from the stack and multiply it by the register value, storing the result in the register.
DIV : Pop a value from the stack and divide the register value by the popped stack value, storing the integer result back in the register.
REMAINDER : Pop a value from the stack and divide the register value by the popped stack value, storing the integer remainder of the division back in the register.
POP : Remove the topmost item from the stack and place it in the register.
PRINT : Print the register value.

Further Exploration:
Refactor the minilang function to include some error handling. 
In particular, the function should detect and report empty stack conditions 
(trying to use a value from the stack when there are no values), and invalid 
tokens in the program. Ideally, the function should return an error message 
if an error occurs, or None if the program runs successfully.
"""

def minilang(string):
    stack = []
    register = 0
    commands = string.split()
    for command in commands:
        if command.isdigit() or (command[0] == '-' and command[1:].isdigit()):
            register = int(command)
        elif command == 'POP':
            register = int(stack.pop())
        elif command == 'PUSH':
            stack.append(register)
        elif command == 'ADD':
            register += int(stack.pop())
        elif command == 'SUB':
            register -= int(stack.pop())
        elif command == 'MULT':
            register *= int(stack.pop())
        elif command == 'DIV':
            register //= int(stack.pop())
        elif command == 'REMAINDER':
            register %= int(stack.pop())
        elif command == 'PRINT':
            print(f'Register Value: {register}')

minilang('PRINT')
# 0

minilang('5 PUSH 3 MULT PRINT')
# 15

minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
# 5
# 3
# 8

minilang('5 PUSH POP PRINT')
# 5

minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
# 5
# 10
# 4
# 7

minilang('3 PUSH PUSH 7 DIV MULT PRINT')
# 6

minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
# 12

minilang('-3 PUSH 5 SUB PRINT')
# 8

minilang('6 PUSH')
# (nothing is printed)
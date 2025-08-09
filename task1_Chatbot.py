#define possible math operations
math_operations = {
    'addition': '+',
    'subtraction': '-',
    'multiplication': '*',
    'division': '/'
}

name = input("Please enter your name: ").capitalize() # takes the name from the user

print("\n** Available operations:")   

for (op, symbol) in math_operations.items(): # iterates through the possible math operations and prints them
    print(f" - {op.capitalize()} ({symbol})")

print("** Expression: num1 op_symbol num2")
print("** To Quit type: exit\n")


while True: # loop to keep asking for input until 'exit' is typed
    expression = input(f"Hi {name}, Enter the math expression (ex: 4 + 3): ")
    if(expression.lower() == "exit"): break # checks for exit input to quit
    expression = expression.split() # splits the input to a list to store the numbers and operation
    

    #checks if the opertion is in the dictionary and if the input contains three parts (num1 op num2)
    if (len(expression) == 3 and expression[1] in math_operations.values()): 

        num1 = float(expression[0])
        num2 = float(expression[2])
        op = expression[1]

        result = 0

        match op: # checks the operation type and preforms it
            case '+':
                result = num1 + num2
            case '-':
                result = num1 - num2
            case '*':
                result = num1 * num2
            case '/':
                if (num2 == 0):
                    print("ERROR: Can't divid by zero!")
                    continue
                result = num1 / num2
        
        print(f"Result = {result}")
    else: # if the operation is not in the dictionary
        print(f"Sorry {name}, I don't understand the question :(")


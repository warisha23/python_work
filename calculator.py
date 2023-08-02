class Calculator:
    '''A simple calculator file'''

    # this functions adds two numbers
    def add(num1 , num2):
        return num1 + num2

    # this functions subtracts two numbers
    def subtract(num1 , num2):
        return num1 - num2

    # this functions divides two numbers
    def divide(num1 , num2):
        return num1 / num2

    # this functions multiplies two numbers
    def multiply(num1 ,num2):
        return num1 * num2
    
# Take input from the user
    choice = (input(" which operator (+, -, *, /): "))
 
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
 
    if choice == '+':
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '-':
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == '*':
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == '/':
        print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("Invalid input")

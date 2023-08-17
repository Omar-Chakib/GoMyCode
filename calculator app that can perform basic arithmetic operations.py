def calculator(num1, num2):
    operator = input("Enter an operator (+, -, *, /) or 'quite' to quit: ")

    if operator.lower() == 'quit':
        return None  # Indicates the user wants to exit

    if operator != '+' and operator != '-' and operator != '*' and operator != '/':
        return "Invalid operator"

    if operator == '/' and num2 == 0:
        return "Cannot divide by zero"

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    else:
        result = num1 / num2

    return result

while True:
    num1 = float(input("Enter the first number (or type 'quit' to quit): "))
    
    if num1.lower() == 'exit':
        break
    
    num2 = float(input("Enter the second number: "))
    
    result = calculator(num1, num2)
    
    if result is None:
        print("Exiting calculator.")
        break
    
    print("Result:", result)

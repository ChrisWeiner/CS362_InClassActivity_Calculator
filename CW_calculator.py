def addition(x,y):
    return x+y

def subtraction(x,y):
    return x-y

def multiplication(x,y):
    return x*y

def division(x,y):
    if(float(y) == 0):
        print("Cannot divide by zero")
        return
    else:    
        return x/y
try:
    print("Enter the first number: ")
    input1 = input()
    x = float(input1)
    print("Enter the second number: ")
    input2 = input()
    y = float(input2)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("Enter the number of the operation")
    input3 = input()
    operation = float(input3)
    if(operation == 1):
        result = addition(x,y)
        print("Result: " + str(result))
    elif(operation == 2):
        result = subtraction(x,y)
        print("Result: " + str(result))
    elif(operation == 3):
        result = multiplication(x,y)
        print("Result: " + str(result))
    elif(operation == 4):
        result = division(x,y)
        print("Result: " + str(result))
    else:
        print("Next time, please enter a valid number")
except ValueError:
    print("Either " + str(x) + " or " + str(y) + " is not a valid number, or not a valid input")
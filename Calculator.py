# Python Program to Make a Simple Calculator
def multipication(num1, num2):
    return num1 * num2
def addition(num1, num2):
    return num1 + num2
def subtraction(num1, num2):
    return num1 - num2
def divide(num1, num2):
    while True:
        try:
            answer = num1/num2
            return(answer)
            break
        except ZeroDivisionError:
            num2 = int(input('Please enter a number other than zero: '))
while True:
    value1 = int(input("Enter 1st number: "))
    value2 = int(input("Enter 2nd number: "))
    print("Select operation 1-Division, 2-Multiplication, 3-Addition, 4-Subtraction")
    operation = int(input("Choose operation 1/2/3/4: "))
    while True:
        if operation == 1:
            print(value1, "/", value2, "=", divide(value1, value2))
            break
        elif operation == 2:
            print(value1, "*", value2, "=", multipication(value1, value2))
            break
        elif operation == 3:
            print(value1, "+", value2, "=", addition(value1, value2))
            break
        elif operation == 4:
            print(value1, "-", value2, "=", subtraction(value1, value2))
            break
        else:
            operation = int(input("Enter correct operation "))
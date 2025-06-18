def add(num1, num2):
    answer = num1 + num2
    return answer

def subtract(num1, num2):
    answer = num1 - num2
    return answer

def multiply(num1, num2):
    answer = num1 * num2
    return answer

def divide(num1, num2):
    answer = num1 / num2
    return answer

def calculate(operation, num1, num2):
    if operation == "add":
        ans = add(num1, num2)
    elif operation == "subtract":
        ans = subtract(num1, num2)
    elif operation == "multiply":
        ans = multiply(num1, num2)
    elif operation == "divide":
        ans = divide(num1, num2)
    else:
        print("error")
        return
    print(ans)

calculate("subtract", 7, 3)
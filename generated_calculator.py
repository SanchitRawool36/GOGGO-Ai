def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"

# Example usage
result = calculate(10, 5, '+')
print(result)  # Output: 15

result = calculate(10, 5, '-')
print(result)  # Output: 5

result = calculate(10, 5, '*')
print(result)  # Output: 50

result = calculate(10, 5, '/')
print(result)  # Output: 2.0

result = calculate(10, 5, '%')  # Invalid operator
print(result)  # Output: Error: Invalid operator

result = calculate(10, 0, '/')  # Division by zero
print(result)  # Output: Error: Division by zero
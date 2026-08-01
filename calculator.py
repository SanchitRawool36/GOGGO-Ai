def calculate():
    while True:
        try:
            operation = input("Enter an operation (+, -, *, /) or 'exit' to quit: ")
            if operation == 'exit':
                break
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    print("Error: Division by zero.")
                    continue
                result = num1 / num2
            else:
                print("Invalid operation. Please try again.")
                continue

            print(f"Result: {result}")

        except ValueError:
            print("Invalid input. Please enter numbers only.")

calculate()
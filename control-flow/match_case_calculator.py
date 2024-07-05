# Function to perform the calculation based on the operation
def calculate(num1, num2, operation):
    match operation:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            if num2 != 0:
                return num1 / num2
            else:
                return "Cannot divide by zero."
        case _:
            return "Invalid operation."

# Main function
def main():
    # Prompt the user for two numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Ask for the operation
    operation = input("Choose the operation (+, -, *, /): ").strip()

    # Perform the calculation
    result = calculate(num1, num2, operation)

    # Output the result
    print(f"The result is: {result}")

# Run the main function
if __name__ == "__main__":
    main()

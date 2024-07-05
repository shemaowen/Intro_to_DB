# multiplication_table.py

# Main function
def main():
    try:
        # Ask the user for a number
        number = int(input("Enter a number to see its multiplication table: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return
                                                   
    # Generate and print the multiplication table
    print(f"Multiplication table for {number}:")
    for i in range(1, 11):
        product = number * i
        print(f"{number} * {i} = {product}")

# Run the main function
if __name__ == "__main__":
    main()

def print_formatted(number):
    # Calculate the width needed for binary representation of 'number'
    width = len(bin(number)) - 2  # Subtract 2 to exclude '0b' prefix

    # Print the formatted values
    for i in range(1, number + 1):
        decimal_str = str(i)
        octal_str = oct(i)[2:]  # Remove '0o' prefix
        hexadecimal_str = hex(i)[2:].upper()  # Remove '0x' prefix and capitalize
        binary_str = bin(i)[2:]  # Remove '0b' prefix

        # Print values with appropriate padding
        print(f"{decimal_str:>{width}} {octal_str:>{width}} {hexadecimal_str:>{width}} {binary_str:>{width}}")

# Example usage
n = int(input("Enter an integer: "))
print_formatted(n)

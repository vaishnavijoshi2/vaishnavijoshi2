def split_and_join(line):
    # Split the input string into a list of words
    words = line.split(" ")
    
    # Join the words using a hyphen as the separator
    result = "-".join(words)
    
    return result

# Example usage
input_string = "this is a string"
output_string = split_and_join(input_string)
print(output_string)  # Output: "this-is-a-string"

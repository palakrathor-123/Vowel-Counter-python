def count_vowels_iterative(input_string):
    count = 0
    # Define a set of vowels for efficient lookup
    vowels = set("aeiou") 
    # Convert the entire string to lowercase for case-insensitivity
    input_string = input_string.lower()

    for char in input_string:
        if char in vowels:
            count += 1
    return count

# Example Usage:
my_string = "Hello World! This is a test."
vowel_count = count_vowels_iterative(my_string)
print(f"The number of vowels in the string is: {vowel_count}")
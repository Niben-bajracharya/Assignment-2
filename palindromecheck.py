# Write a Python program that checks if a given string is a palindrome.

def is_palindrome(s):
    # Convert the string to lowercase and remove non-alphanumeric characters
    s = ''.join(char.lower() for char in s if char.isalnum())
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Input from the user.
string = input("Enter a string: ")

# Check the input string is a palindrome.
if is_palindrome(string):
    print("Yes, '{}' is a palindrome.".format(string))
else:
    print("No, '{}' is not a palindrome.".format(string))

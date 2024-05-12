
#Write a Python program that prints the following pattern using a nested for loop:
#        *
#        **
#        ***
#        ****
#        *****


# the size of the pattern
size = 5

# loop for rows
for i in range(size):
    # Inner loop for columns
    for j in range(i + 1):
        print("*", end=" ")  # Print * with space
    print()     # Move to the next line

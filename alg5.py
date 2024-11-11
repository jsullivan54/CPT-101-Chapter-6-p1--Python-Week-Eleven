# Open the file for reading
number_list = open('number_list.txt', 'r')  # Corrected filename

# Read all lines from the file
numbers = number_list.readlines()

# Display the numbers
for number in numbers:
    print(number.strip())  # .strip() removes the newline character at the end of each line

# Close the file after reading
number_list.close()

# Open the file for reading
number_list = open('number_list.txt', 'r')  # Corrected filename

# Initialize a variable to hold the total sum
total_sum = 0

# Read all lines from the file
numbers = number_list.readlines()

# Add the numbers and calculate the total sum
for number in numbers:
    total_sum += int(number.strip())  # Convert the string to an integer and add to the sum

# Display the total sum
print("Total sum of numbers:", total_sum)

# Close the file after reading
number_list.close()

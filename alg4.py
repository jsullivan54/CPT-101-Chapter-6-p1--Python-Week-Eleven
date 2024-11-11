# Open the file for writing (this will create the file if it doesn't exist)
number_list = open('number_list.txt', 'w')  # Corrected the filename

# Loop through numbers 1 to 100 and write each number to the file
for num in range(1, 101):
    number_list.write(str(num) + '\n')

# Close the file after writing
number_list.close()

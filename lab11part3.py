#Name: Johnathan Sullivan

#Date: 11/08/2024

#lab11part3

# THis program helps a sales manager process and summarize the sales data for their salespeople

# The program asks the user for the filename of the sales data file./
# The file name is not specific and asks the user for the file name they want to access
# It is NOT inclusive to a test file... It can be a magnitude of file names each with its own file name




#Define the main function
def main():
    keep_going = True
    while keep_going: #make the loop
        try:
            # Ask for the filename input
            filename = input('Please enter a filename: ')
            # open the file.
            my_file = open(filename, 'r')

        except FileNotFoundError:
            # File Error
            print(f'The file "{filename}" does not exist! Please enter a valid filename.')

        else:
            # If the file is found, proceed
            print('File was found. You can continue.')
            keep_going = False  # Exit loop after file is successfully opened
            print(f'We are continuing with our program.')

            # Initialize total sales and transaction count
            total_sales = 0.0
            num_transactions = 0

            # Read lines from the file
            sales = my_file.readlines()

            # Calculate the total sales
            for number in sales:
                try:
                    sale = float(number.strip())  # Convert line to a float
                    total_sales += sale
                    num_transactions += 1
                except ValueError:
                    print(f" A Non-integer character was found in your file. I'll go ahead and skip line: {number.strip()}")

            # Calculate the average sale price
            average_sale = get_average(total_sales, num_transactions)

            # Display the results formatted as currency
            print("\nSales Summary:") # Display the Sales Summary to the end-user

            print(f"Number of Sales Transactions: {num_transactions}") # Display the Sales Summary to the end-user

            print(f"Total Sales: ${total_sales:,.2f}") # Display the Sales Summary to the end-user

            print(f"Average Sale Price: ${average_sale:,.2f}") # Display the Sales Summary to the end-user

            #Close the file (I was thinking about using with statement to close automatically and decided against)
            my_file.close()

# Create get_average function take notice of (total_sales, num-transactions)
def get_average(total_sales, num_transactions):
    if num_transactions == 0:
        return 0.0
    return total_sales / num_transactions




# Close the Program
main()


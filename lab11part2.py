#Johnathan Sullivan AKA Bruce Wayne Jung

#Date: 11/08/2024

#lab11part2

# This program asks the user for their name, writes it to a file, saves the file as a .txt file labeled as/
# end_user_name.txt



# define the main function
def main():

# Intro
    print('Welcome to my name writer!!!! ')

# Ask the end user for their name
    end_user_name = input(f'Gimme your name sucka! (Enter it here): ')

# Open the File end_user_name.txt
    myfile = open(f'end_user_name.txt', 'w')

#write the name the end user entered
    myfile.write(end_user_name + '\n')

#close the file
    myfile.close()

# Tell these fools what happened
print('The names were written to end_user_name.txt')
#end
main()





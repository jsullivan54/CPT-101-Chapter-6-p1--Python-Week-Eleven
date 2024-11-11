keep_going = True
while keep_going == True:
    try:
        filename = input('Please enter a filename: ')
        my_file = open(filename, 'r')

    except FileNotFoundError:
        print(f'the file does not exist!!! Please enter a valid filename')

    else:
        print('File was found you can continue')
        keep_going = False
        print(f'We are continuing with our program.')







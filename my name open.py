

def main():
    infile = open('my_name.txt', 'r')

    line1 = infile.readline()



    line1 = line1.rstrip('\n')


    infile.close()

    print(line1)


main()


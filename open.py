def main():
    infile = open('myname.txt', 'r')

    line1 = infile.readline()


    line1 = line1.rstrip('\n')

    infile.close()

    print(line1)

main()


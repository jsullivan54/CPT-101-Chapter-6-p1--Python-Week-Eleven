def main():
    infile = open('../Module 10 /numbers.txt', 'r')

    num1 = int(infile.readline())
    num2 = int(infile.readline())
    num3 = int(infile.readline())
    num4 = int(infile.readline())
    infile.close()
    avg = num1 + num2 + num3 +num4 / 4
    print(f'The numbers are: {num1}, {num2}, {num3}, {num4}')
    print(f'Their average is: {avg}')

main()
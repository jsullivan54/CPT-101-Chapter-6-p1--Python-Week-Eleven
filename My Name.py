

def main():
    my_name = ('Johnathan')
    myfile = open('my_name.txt' , 'w')
    myfile.write(my_name + '\n')
    myfile.close()
main()
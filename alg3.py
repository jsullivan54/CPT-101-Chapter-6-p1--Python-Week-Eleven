number_list = open('number_list .txt' , 'w')
for num in range (1, 101):
    number_list.write(str(num)+'\n')

number_list.close()

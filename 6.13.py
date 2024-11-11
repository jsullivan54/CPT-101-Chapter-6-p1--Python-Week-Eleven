def main():
    num_emps = int(input('How many employee records'+ 'do you want to create?'))
    emp_file = open('employees.txt', 'w')
    for count in range (1, num_emps +1):
        print(f'Enter data for employee#{count}')
        name = input('Name')
        id_num = input('ID number')
        dept = input('Department')

        emp_file.write(f'{name}/n')
        emp_file.write(f'{id_num}/ n')
        emp_file.write(f'{dept}/ n')
        print()
        emp_file.close()
        print('Employee records written to employees.txt')
main()

def number_input():
    while True:
        number = input('Number: ')
        number_s = number.replace('.', "")
        if number_s.isdigit():
            number = float(number)
            return number
        else:
            print('Not a number you silly goose, choose a number')

def operator_input():
    while True:
        operator = input('Operator: + - * / ')
        if operator in ('+', '-', '*', '/'):
            return operator
        else:
            print('Please choose an operator')
    
def calc(x, y, operator):
    if operator == '+':
        operator = x + y
        return operator
    if operator == '-':
        operator = x - y
        return operator
    if operator == '*':
        operator = x * y
        return operator
    if operator == '/':
        operator = x / y
        return operator

first_num = number_input()
operator = operator_input()
second_num = number_input()

rekenen = calc(first_num, second_num, operator)
rekenen = format(rekenen, '.1f')
print(rekenen)
    


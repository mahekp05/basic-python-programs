#Mahek Patel
#U10206053
#Basic operations using lambda functions - creating calculator using lamda functions

#if-else statement using lamdba calcuating values
#prints answers as well
def calc(operator):
    if operator == 'add' or operator == '+':
        val = lambda x,y: x + y
        n_operator = '+'
        print(f'{num1} {n_operator} {num2} = {val(num1, num2)}')
    elif operator == 'subtract' or operator == 'sub' or operator == '-':
        val = lambda x,y: x - y
        n_operator = '-'
        print(f'{num1} {n_operator} {num2} = {val(num1, num2)}')
    elif operator == 'multiplication' or operator == 'multiply' or operator == '*':
        val = lambda x,y: x * y
        n_operator = '*'
        print(f'{num1} {n_operator} {num2} = {val(num1, num2)}')
    elif operator == 'floating point division' or operator == 'division' or operator == '/':
        val = lambda x,y: x/y
        n_operator = '/'
        print(f'{num1} {n_operator} {num2} = {val(num1, num2)}')
    elif operator == 'integer division' or operator == 'int division' or operator == '//':
        val = lambda x,y: x//y
        n_operator = '//'
        print(f'{num1} {n_operator} {num2} = {val(num1, num2)}')
    elif operator == 'modulus operator' or operator == 'mod division' or operator == '%':
        val = lambda x,y: x%y
        n_operator = '%'
        print(f'{num1} {n_operator} {num2} = {val(num1, num2)}')
    elif operator == 'exponent' or operator == 'exp' or operator == '^':
        val = lambda x,y: x**y
        n_operator = '^'
        print(f'{num1} {n_operator} {num2} = {val(num1, num2)}')
    else:
        n_operator = operator
        print(f'{num1} {n_operator} {num2} = Invalid operation')


#gathering user input
operator = input('Enter the operation as a symbol (e.g. + for addition):')
num1,num2 = input('Enter two values, separated by a space:').split()
num1 = float(num1)
num2 = float(num2)

#calling function 
operator = operator.lower()
calc(operator)








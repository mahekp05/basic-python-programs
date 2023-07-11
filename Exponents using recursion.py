#Mahek Patel
#U10206053
#Exponents using recursion -- using recursive functions to calculate a value with it's base and exponent

#recursive function calculating exponents
def exponent(power,base):
    if power == 0:
        return 1
    elif power == 1:
        return base 
    else:
        return base * exponent(power-1,base)
        


#gathering user input
user_num = int(input('Enter the base:'))
user_exp = int(input('Enter a whole number between 2 and 50:'))

#validating user input using while loop
while 2 < user_exp > 50:
    user_exp = int(input('Invalid. Please enter a whole number between 2 and 50:'))

#store and print answer
f_ans = exponent(user_exp,user_num)
print(f'{user_num} raised to the power of {user_exp} is {f_ans}')

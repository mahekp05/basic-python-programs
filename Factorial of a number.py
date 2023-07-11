#Mahek Patel
#U10206053
#Factorial of a number --- calculating the factorial of an number

#making sure input is an positive number
while (num := int(input('Enter a nonnegative integer: '))) <0:
    num = int(input('Invalid. Enter a nonnegative integer: '))

#answer variable
ans = num

#calculating factorial
if num > 0:
    x = 0
    end = num - 1
    while x < num:
        if end > 0:
            ans = ans * end
        else:
            ans = ans* 1
        end = end -1
        x = x + 1
else: #factorial value 0 the ans is 1
    ans = 1

#comma seperation in factorial
a = list(str(ans))
for x in range(len(a)-3,0,-3):
    a.insert(x,',')
    
print('The factorial of ',num,' is ', end  = '')
for i in a:
    print(i, end = '')




    

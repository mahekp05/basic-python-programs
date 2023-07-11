#Mahek Patel
#U10206053
#Good ol’ Guessing Game -- try to guess the right number (10 tries given)

#importing random module
import random as r

#generating random number for gam
rand_num = r.randrange(1,100)

#user input
input1 = int(input('Enter a number between 1 and 100 (inclusive): '))

#loop analyzing each input given for each try
x = 0
guess = 1
while x < 10:
    #makes sure input is between 0 and 100
    if input1 < 1:
        input1 = int(input('Really? Enter another guess between 1 to 100: '))
    elif input1 > 100:
        input1 = int(input('Very funny. Enter a number between 1 and 100 (inclusive): '))
    #if user guesses number right and on which try they guess right
    if input1 == rand_num:
        print(f'You guessed it right!! You got it in {guess} guesses!')
        break
    #gives user clue on how far away their guess is from actual num
    if 1 <= input1 <= 100:
        if input1 > rand_num:
            input1 = int(input('Too high. Enter another guess: '))
            guess += 1
            x += 1
        else:
            input1 = int(input('Too low. Enter another guess: '))
            guess += 1
            x += 1
#if they don't get answer within 10 tries
if input1 != rand_num:
    print(f'Sorry, the number was {rand_num}')

        
    

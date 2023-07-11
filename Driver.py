#Mahek Patel
#U10206053
#driver file -- runs the game for user (keeping track of right and wrong answers)

#importing questions
from TriviaQuestions import TriviaQuestions

#scores and score tracker
scores = [0,0]
turn = 0
questions = TriviaQuestions()

#questions alternation
for q in questions:
    if turn%2 == 0:
        print('Question for the first player:')
    else:
        print('Question for the second player:')


    print(str(q))
    
    choice = int(input('Enter your solution (a number between 1 and 4):'))

    if choice == q.correctans:
        print('This is the correct answer\n')
        scores[turn%2] += 1
    else:
        print(f'That is incorrect. The correct answer is {q.correctans}.\n')

    turn +=1


print(f'The first player earned {scores[0]} points.')
print(f'The second player earned {scores[1]} points.')

winner = 'first' if scores[0] > scores[1] else 'second'

print(f'The {winner} player wins the game.')

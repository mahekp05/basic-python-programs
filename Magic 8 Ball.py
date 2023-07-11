#Mahek Patel
#U10206053
#Magic 8 Ball - get your questions answered with this magic 8ball code

#import random module
import random as r

#void function generating random answer from local list
def fortune(random):
    ans = ['It is certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes-definitely.', 'You may rely on it.', 'As I see it, yes.',
       'Most likely.', 'Outlook good.', 'Yes.', 'Signs point to yes.', 'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.',
       'Cannot predict now.', 'Concentrate and ask again.', 'Don\'t count on it.', 'My reply is no.', 'My sources say no.',
       'Outlook not so good.', 'Very doubtful.']
    print(ans[random])



#main function calling void function with loop to ask more questions
def main():

    question = input('What is your question? ').lower() 
    while question != 'no':
        rand_gen = r.randint(0,19)
        fortune(rand_gen)
        question = input('Would you like to ask another question?').lower()
        if question != 'no':
            question = input('What is your question? ').lower()
        else:
            break
            


#calls main function
main()

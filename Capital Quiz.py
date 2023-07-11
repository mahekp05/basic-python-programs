#Mahek Patel
#U10206053
#Capital Quiz -- a quiz to test you on your knowledge of the USA CAPITALS!!!!

import random as r

capitals_USA = {'Alabama':'Montgomery','Alaska':'Juneau','Arizona':'Phoenix','Arkansas':'Little Rock',
                'California':'Sacramento','Colorado':'Denver','Connecticut':'Hartford',
                'Delaware':'Dover','Florida':'Tallahassee','Georgia':'Atlanta',
                'Hawaii':'Honolulu','Idaho':'Boise','Illinois':'Springfield',
                'Indiana':'Indianapolis','Iowa':'Des Moines','Kansas':'Topeka',
                'Kentucky':'Frankfort','Louisiana':'Baton Rouge','Maine':'Augusta',
                'Maryland':'Annapolis','Massachusetts':'Boston','Michigan':'Lansing',
                'Minnesota':'Saint Paul','Mississippi':'Mississippi','Missouri':'Jefferson City',
                'Montana':'Helena','Nebraska':'Lincoln', 'Nevada':'Carson City',
                'New Hampshire':'Concord','New Jersey':'Trenton', 'New Mexico':'Santa Fe',
                'New York':'Albany', 'North Carolina':'Raleigh','North Dakota':'Bismarck',
                'Ohio':'Columbus','Oklahoma':'Oklahoma City', 'Oregon':'Salem',
                'Pennsylvania':'Harrisburg','Rhode Island':'Providence',
                'South Carolina':'Columbia','South Dakota':'Pierre', 'Tennessee':'Nashville',
                'Texas':'Austin','Utah':'Salt Lake City', 'Vermont':'Montpelier',
                'Virginia':'Richmond','Washington':'Olympia', 'West Virginia':'Charleston',
                'Wisconsin':'Madison','Wyoming':'Cheyenne'}

random = r.randint(0,49)

#convert from dict to list for states
state_list = list(capitals_USA)

state = state_list[random]

c = 0
inc = 0
ans = input(f'What is the capital of {state}? (or enter q to quit): ').title()
##sential value is 'q' 
while ans != 'Q':
    if ans == capitals_USA[state]:
        print('That is correct.')
        c += 1
        random = r.randint(0,49)
        state_list = list(capitals_USA)
        state = state_list[random]
        ans = input(f'What is the capital of {state}? (or enter q to quit): ').title()
    else:
        print('That is incorrect.')
        inc += 1
        random = r.randint(0,49)
        state_list = list(capitals_USA)
        state = state_list[random]
        ans = input(f'What is the capital of {state}? (or enter q to quit): ').title()
print(f'You had {c} correct responses and {inc} incorrect responses.')
    



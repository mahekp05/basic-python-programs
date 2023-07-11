#Mahek Patel
#U10206053
#The Price is Right game - selecting the winner with the closest bid 

import random as r 

prize = r.randrange(1000,5001)
print(prize)


bids = []
num = 1

#adding input into an list
i = 0
while(i < 4):
    bid = int(input(f'Player {num}, what is your bid? '))
    bids.append(bid)
    num = num+1
    i = i + 1

#all over bids code
if bids[0] > prize and bids[1] > prize and bids[2] > prize and bids[3] > prize:
    print(f'Buzz! Aww... everyone has overbid! ')

#exact same price
elif bids[0] == prize or bids[1] == prize or bids[2] == prize or bids[3] == prize:
    print(f'Ding Ding Ding! One player got it exactly right and gets $500!\nActual price is {rand_price}! Player {bids.index(rand_price)+1}, come on up!')

#some overbid/underbid and choosing value closest to the prize
else:
    underbid = []
    m=0
    n = 0
    winner = 0
    for x in bids:
        diff = prize - bids[m]
        if diff > 0:
            underbid.append(bids[m])
            m += 1
    for y in underbid:
        if underbid[n] > winner:
            winner = underbid[n]
            n+=1
    print(f'Actual price is {prize}! Player {bids.index(winner)+1}, come on up!')

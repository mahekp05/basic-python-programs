#Mahek Patel
#U10206053
#Area of a flower

radius = float(input('Enter the radius of the flower: '))

#PETAL
#semi-circle radius forumla 
r1 = (radius/2)

#semi-circle radius squared
r_sq = r1**2

#defining pi
pi = 3.14159

#semi-cirlce area calculation
semi = (1/2)*(pi)*(r_sq)

#total area added for flower
area = (semi*4) + (radius*radius)

print(f'The area of the flower is {area} square units.')

#Mahek Patel
#U10206053
#Drawing Polygons with the turtle module -- drawing a polygon based on user input and classifying what kind of polygon has been drawn

import turtle

#user input for side and length
user_side = turtle.numinput('Side Entry','Enter the number of sides', default = 3, minval = 3, maxval = 12)
user_length = turtle.numinput('Length Entry', 'Enter the length of each side', default = 50, minval = 50, maxval = 250)

#converting from float to int values
user_side = int(user_side)
user_length = int(user_length)

#calculating which angle to turn at 
angle = (180 * (user_side - 2) )/user_side
turn_angle = 180 - angle

#loop to help draw the shape
for x in range(user_side):
    turtle.forward(user_length)
    turtle.right(turn_angle)

#classifying what kind of shape has been drawn based on the number of sides
if user_side == 3:
    turtle.write('Triangle')
elif user_side == 4:
    turtle.write('Quadrilateral ')
elif user_side == 5:
    turtle.write('Pentagon')
elif user_side == 6:
    turtle.write('Hexagon')
elif user_side == 7:
    turtle.write('Heptagon')
elif user_side == 8:
    turtle.write('Octagon')
elif user_side == 9:
    turtle.write('Nonagon')
elif user_side == 10:
    turtle.write('Decagon')
elif user_side == 11:
    turtle.write('Hendecagon')
elif user_side == 12:
    turtle.write('Dodecagon')


#Mahek Patel
#U10206053
#slope_of_a_line


#gather coordinates for first point
x1,y1 = input('Enter the coordinates of the first point: ').split()
x1 = float(x1)
y1 = float(y1)

#gather coordinates for second point
x2,y2 = input('Enter the coordinates of the first point: ').split()
x2 = float(x2)
y2 = float(y2)

#calculates slope
slope = (y2 - y1)/(x2-x1)

#printing slope
print(f'The slope of the line that connects two points ({x1} , {y1}) and ({x2} , {y2}) is {slope:.3f}')

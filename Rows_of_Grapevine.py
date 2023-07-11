#Mahek Patel
#U10206053
#Rows of Grapevine: calculates the amount of grapvine there is space for based on user input

#gathering input from user (length, space used by end-post assembly, distance between each vine)
length = int(input('Enter the length of the row, in feet: '))
space_post = float(input('Enter the amount of space, in feet, used by an end-post assembly: '))
space_vine = int(input('Enter the distance, in feet, between each vine: '))

#calculates the amount of space for grapevines based off the user's input
row_grapevine = (length - (2 * space_post)) / space_vine

#prints amount of grapvine 
print(f'You have enough space for {row_grapevine:.1f} vines.')

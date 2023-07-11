#Aastha Sangani
#U73625733

from polygons import regularPolygon

def main():
    polygon = regularPolygon()

    num_side = int(input('Enter the number of sides (>=3): '))
    while num_side < 3:
        num_side = int(input('Invalid entry. Re-enter the number of sides (>=3): '))
    polygon.setSides(num_side)

    length_size = float(input("Enter the length of each side (>=0.1): "))
    while length_size < 0.1:
        length_size = float(input("Invalid side length. Enter the length of each side (>=0.1): "))
    polygon.setLength(length_size)

    print(f'The polygon has {polygon.getSides()} sides. Each side is {polygon.getLength()} units in length.')
    print(f'The perimeter of the polygon is {polygon.perimeter():.3f} units and it\'s area is {polygon.area():.3f}')
    

main()

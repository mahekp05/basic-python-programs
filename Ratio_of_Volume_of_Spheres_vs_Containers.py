#Mahek Patel
#U10206053
#Ratio of Volume of Spheres vs Containers -- calculating ratio of volume spheres occupy in a cylinder

import math

#gather user input for number of spheres and it's diameter
num_sphere = int(input('Enter the number of spheres to be placed in the container: '))
diameter = float(input('Enter the diameter of each sphere (in inches): '))

#calculate radius
radius = diameter/2

#calculate container height
container_height = diameter * num_sphere

#calculate volume of spheres and cylinder
volume_sphere = (4/3)*(math.pi)*pow(radius,3)
volume_3sphere = volume_sphere * num_sphere
volume_cyliner = (math.pi)*(pow(radius,2))*(container_height)

#calculate % of cylinder occuped by sphere
percentage_vol = (volume_3sphere/volume_cyliner)*100

#print all data calculated for sphere and cyliner
print(f'The container would need to be at least {container_height} inches to hold the {num_sphere} spheres.')
print(f'The {num_sphere} spheres will occupy {percentage_vol:.2f}% of the container.')

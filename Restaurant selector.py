#Mahek Patel
#U10206053
#Restaurant Selector - gives restaurant choices based on the parties dietary prefrences

vegetarian = input('Is anyone in your party a vegetarian? ')
vegan = input('Is anyone in your party a vegan? ')
g_free = input('Is anyone in your party a gluten free? ')


print('Here are your restaurant choices:')

#if else statement checkibg based on party
#all options yes
if vegetarian == 'Yes' and vegan == 'Yes' and g_free == 'Yes':
    print('True Food Kitchen')
#vegetarian - yes and gluten free - yes
elif vegetarian == 'Yes' and g_free == 'Yes':
    print('Gourmet Pizza Company')
    print('True Food Kitchen')
#vegetarian - yes
elif vegetarian == 'Yes':
    print('Bella’s Italian Restaurant')
    print('Gourmet Pizza Company')
    print('True Food Kitchen')
#vegan - yes
elif vegan == 'Yes' :
    print('True Food Kitchen')
#gluten free - yes
elif g_free == 'Yes' :
    print('True Food Kitchen')
    print('Gourmet Pizza Company')
#no specific prefrence
else:
    print('Fleming’s Prime Steakhouse')






#Mahek Patel
#U10206053

from Retail_class import Retail_Item
def main():
    t1 = input('Name of item 1: ')
    amount1 = int(input('Amount of item 1: '))
    p1 = float(input('Price of item 1: '))

    type2 = input('Name of item 2: ')
    amount2 = int(input('Amount of item 2: '))
    p2 = float(input('Price of item 2: '))

    item1 = Retail_Item(t1,amount1,p1)
    item2 = Retail_Item(t1,amount2,p2)

    print('Here is the summary of the items you added:')

    print(f'{"Item".ljust(15)}{"Amount".rjust(10)}{"Price".rjust(15)}')

    print('-----------------------------------------')

    print(item1)
    print(item2)

main()

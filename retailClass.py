#Aastha Sangani
#73625733

class Retail_Item:
    def __init__(self,atype,amt,price):
        self.__type = atype
        self.__amount = amt
        self.__price = price

    def __str__(self):
        return f'{self.__type.ljust(15)}{str(self.__amount).rjust(10)}{str(self.__price).rjust(15)}$'
        
    
    

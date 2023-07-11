#Mahek Patel
#U10206053
#Questions Class - creating class for questions for trivia games

class Questions:
    def __init__(self, question, ans1, ans2, ans3, ans4, ans):
        self.__question = question
        self.__answer1 = ans1
        self.__answer2 = ans2
        self.__answer3 = ans3
        self.__answer4 = ans4
        self.correctans = ans

    def __str__(self):
        print_str = ''
        print_str  += self.__question + '\n'
        print_str  += '1. ' + self.__answer1 + '\n'
        print_str  += '2. ' + self.__answer2 + '\n'
        print_str  += '3. ' + self.__answer3 + '\n'
        print_str  += '4. ' + self.__answer4 + '\n'

        return print_str  

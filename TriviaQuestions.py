#Mahek Patel
#U10206053
#Trivia Questions -- storess questions for the trivia

#importing class 
from QuestionsClass import Questions

#adding questions to a list using class
def TriviaQuestions():
    questions = []

    questions.append(Questions('How many days are in a lunar year?','354','365','243','379',1))
    questions.append(Questions('What is the largest planet?','Mars','Jupiter','Earth','Pluto',2))
    questions.append(Questions('What is the largest kind of whale?','Orca whale','Humpback whale','Beluga whale','Blue whale',4))
    questions.append(Questions('Which dinosaur could fly?','Triceratops','Tyrannosaurus Rex','Pteranodon','Diplodocus',3))
    questions.append(Questions('Which of these Winnie the Pooh characters is a donkey?','Pooh','Eeyore','Piglet',' Kanga',2))
    questions.append(Questions('What is the hottest planet?','Mars','Pluto','Earth','Venus',4))
    questions.append(Questions('Which dinosaur had the largest brain compared to body size?','Troodon','Stegosaurus','Ichthyosaurus','Gigantoraptor',1))
    questions.append(Questions('What is the largest type of penguins?','Chinstrap penguins','Macaroni penguins','Emperor penguins','White-flippered penguins',3))
    questions.append(Questions('Which children\'s story character is a monkey?','Winnie the Pooh','Curious George','Horton','Goofy',2))
    questions.append(Questions('How long is a year on Mars?','550 Earth Days','498 Earth days','126 Earth days',' 687 Earth days',4))

    return questions

    


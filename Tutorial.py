from abc import ABC, abstractmethod

class TutorialInterface(ABC):
    @abstractmethod
    def __init__(self, ID, tutorial_description, category):
        pass

    @abstractmethod
    def check_input(self):
        pass

    @abstractmethod
    def displayAnswer(self):
        pass

class Tutorial(TutorialInterface):

    def __init__(self, ID, tutorial_description, category):
        self.ID = ID
        self.tutorial_description = tutorial_description
        self.category = category

    def check_input(self, input):
        b = open("bSolution.txt", "r")
        i = open("iSolution.txt", "r")
        h = open("hSolution.txt", "r")

        if(input == b.read()):
            print("Correct!")

        elif(input == i.read()):
            print("Correct!")

        elif(input == h.read()):
            print("Correct!")

        else:
            print("Incorrect!")

        return

    def displayAnswer(self):
        #show all tutorial information
        print("")


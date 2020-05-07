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

    def check_input(self):
        correct = None
        if input("^print('Hello World')"):
            correct = True
        else:
            correct = False
        print(correct)
        return

    def displayAnswer(self):
        #show all tutorial information
        print("")

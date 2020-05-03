from abc import ABC, abstractmethod

class TutorialInterface(ABC):
    @abstractmethod
    def __init__(self, ID, tutorial_description, category):
        pass

    @abstractmethod
    def check_input(self):
        pass

    @abstractmethod
    def display(self):
        pass

class Tutorial(TutorialInterface):

    def __init__(self, ID, tutorial_description, category):
        self.ID = ID
        self.tutorial_description = tutorial_description
        self.category = category

    def check_input(self):
        return

    def display(self):
        #show all tutorial information
        print("")


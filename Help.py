from abc import ABC, abstractmethod

class HelpInterface(ABC):
    @abstractmethod
    def __init__(self, assistant, chat_ID):
        pass
        
    @abstractmethod
    def connect_to_chat(self):
        pass

    @abstractmethod
    def help_form(self):
        pass

class Help(HelpInterface):
    def __init__(self, assistant, chat_ID):
        self.assistant = assistant
        self.chat_ID = chat_ID
        
    def connect_to_chat(self):
        print("connect to help")

    def help_form(self):
        print("help form")
        
from abc import ABC, abstractmethod

class MenuInterface(ABC):
    @abstractmethod
    def __init__(self, options, username):
        pass
        
    @abstractmethod
    def open_session(self):
        pass
    
    @abstractmethod
    def open_tutorial(self):
        pass

    @abstractmethod
    def show_profile(self):
        pass

    @abstractmethod
    def show_progress(self):
        pass

    @abstractmethod
    def close(self):
        pass


class Menu(MenuInterface):
    def __init__(self, options, username):
        self.options = options
        self.username = username
        
    def open_session(self):
        print("open session")
        
    def open_tutorial(self):
        print("open tutorial")

    def show_profile(self):
        print("show profile")

    def show_progress(self):
        print("show progress")
        
    def close(self):
        print("close window")
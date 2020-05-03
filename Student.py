from abc import ABC, abstractmethod

class StudentInterface(ABC):
    @abstractmethod
    def __init__(self, username, password, skill_level, email):
        pass
    
    @abstractmethod
    def open_session(self):
        pass
        
    @abstractmethod
    def open_tutorial(self):
        pass

    @abstractmethod
    def save_data(self):
        pass
    
    @abstractmethod
    def close(self):
        pass


class Student(StudentInterface):
    
    # Initializer
    def __init__(self, username, password, skill_level, email):
        self.username = username
        self.password = password
        self.skill_level = skill_level
        self.email = email
    
    def open_session(self):
        return

    def open_tutorial(self):
        return

    def save_data(self):
        return

    def close(self):
        return
    
    
        
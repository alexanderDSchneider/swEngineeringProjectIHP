from abc import ABC, abstractmethod

class SessionInterface(ABC):
    @abstractmethod
    def __init__(self, session_ID, username, tutorial_ID, save_point):
        pass
    
    @abstractmethod
    def send_data(self):
        pass
        
    @abstractmethod
    def end_session(self):
        pass
    
    @abstractmethod
    def retrieve_data(self):
        pass


class Session(SessionInterface):
    def __init__(self, session_ID, username, tutorial_ID, save_point):
        self.session_ID = session_ID
        self.username = username
        self.tutorial_ID = tutorial_ID
        self.save_point = save_point
        
    def send_data(self):
        print("send data")
    
    def end_session(self):
        print("end session")
        
    def retrieve_data(self):
        print("retrieve_data")
        
from abc import ABC, abstractmethod

class AccountInterface(ABC):
    @abstractmethod
    def __init__(self, email, first_name, last_name, phone_no):
        pass
    
    @abstractmethod
    def update(self):
        pass
        
    @abstractmethod
    def show(self):
        pass
    

class Account(AccountInterface):

    def __init__(self, email, first_name, last_name, phone_no):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.phone_no = phone_no

    def update(self, attribute):
        # update the attribute passed to the method
        print("")

    def show(self):
        # show the users account information so that they may validate correctness
        print("")

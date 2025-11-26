from abc import ABC, abstractmethod

class UserServiceInterface(ABC):
    @abstractmethod
    def get_user_by_id(self, user_id: int):
        pass
    
    @abstractmethod
    def login_user(self, username: str, password: str):
        pass

    @abstractmethod
    def register_user(self, username: str, password: str, email: str):
        pass

    @abstractmethod
    def logout_user(self, response):
        pass
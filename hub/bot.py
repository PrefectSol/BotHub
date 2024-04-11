from abc import ABC, abstractmethod

class Bot(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_action(self, state : dict) -> dict:
        pass

from abc import ABC, abstractmethod

class Game(ABC):
    def __init__(self):
        self._players_count = None
        self._is_playing = None
        self._clients = None
        
        
    @abstractmethod
    def __init__(self, settings):
        pass

    @abstractmethod
    def run(self):
        pass
    
    @abstractmethod
    def exit(self):
        pass
        
    @abstractmethod
    def get_state(self, client) -> dict:
        pass
    
    @abstractmethod
    def view_state(self, state : dict):
        pass
    
    @abstractmethod
    def get_target(self) -> list:
        pass

    @abstractmethod
    def get_action(self) -> dict:
        pass
        
    @abstractmethod
    def make_action(self, action : dict):
        pass
    
    @abstractmethod
    def add_client(self, client_info, bot_impl) -> bool:
        pass

    @property
    def players_count(self):
        return self._players_count

    @players_count.setter
    def players_count(self, count):
        self._players_count = count

    @property
    def is_playing(self):
        return self._is_playing

    @is_playing.setter
    def is_playing(self, status):
        self._is_playing = status
        
    @property
    def clients(self):
        return self._clients

    @clients.setter
    def clients(self, clients):
        self._clients = clients

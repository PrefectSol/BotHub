import json
import random
import re

from hub.game import Game


class SeaBattle(Game):
    def __init__(self, settings):
        self._players_count = 2
        self._field_size = 10
        self._is_playing = True
        self._winner = ''
        self._clients = []
        self._fields = []
        
        with open(settings, 'r') as file:
            self._config = json.load(file)
            
        if self._config['first move'] == 1 or self._config['first move'] == 2:
            self._move = self._config['first move'] - 1
        else:
            self._move = random.randint(0, 1)
       
    
    def add_client(self, client_info, bot_impl) -> bool:
        if len(self._clients) < self.players_count:
            match = re.search('class (\\w+)', bot_impl)
            if not match:
                return False
            
            exec(bot_impl)
            bot = eval(match.group(1))
            self._clients.append((client_info, bot()))
            
            return True
        
        return False

    
    def set_state(self):        
        self._fields.append(self._clients[0][1].set_state()['field'])
        self._fields.append(self._clients[1][1].set_state()['field'])
            
    
    def step(self):
        enemy_field = self._fields[(self._move + 1) % 2]
        action = self._clients[self._move][1].make_action(enemy_field)
        
        self._fields[self._move] = self.__calc_field(self._fields[self._move], action)
        self.__next()

    
    def get_state(self) -> dict:
        return {'field1' : self._fields[0], 'field2' : self._fields[1],
                'player_move' : self._clients[self._move],
                'winner': self._winner}
        
    
    def __calc_field(self, field, action):
        pass
        
    
    def __next(self):
        self.__check_winner()
        
        if self._is_playing:
            self._move = (self._move + 1) % 2
        
    
    def __check_winner(self):
        if not any(any(cell != 0 for cell in row) for row in self._fields[self._move]):
            self._winner = self._clients[self._move][0]['from']
            self._is_playing = False
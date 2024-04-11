from datetime import datetime
from hub.TicTacToe.tictactoe import TicTacToe


class Base:
    def __init__(self):
        self._games = {
            'TicTacToe' : TicTacToe
        }
        
        self.log(f'Available games: {list(self._games.keys())}')


    def log(self, msg):
        print(f'[{datetime.now()}] - {msg}')
        
        
    def msg(self, msg, code):
        return {"message": msg}, code

    
    @property
    def games(self):
        return self._games;    
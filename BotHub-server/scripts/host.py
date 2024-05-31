import argparse
import time
import threading
import json
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from flask import Flask, request, render_template
from utils.base import Base
from utils.status import StatusCode

class Host(Base):
    def __init__(self, opt):
        super().__init__()
        self.log(f'Optional arguments: {opt}')
        
        try:        
            with open(opt.config, 'r') as file:
                self._config = json.load(file)
        except Exception as e:
            self.log(f'Error loading configuration: {e}')
            return

        if self._config['game']['name'] not in self.games:
            self.log(f"Error find the game \'{self._games}\' in the available list: {self._config['game']['name']}")
            return
        
        self._game_class = self.games[self._config['game']['name']]
        self._game = self._game_class(self._config['game']['settings'])
        self._clients_count = 0
        self._time = time.time()
        
        path = os.path.dirname(os.path.abspath(__file__))
        self._app = Flask(__name__, template_folder=os.path.join(path, '../site/templates'),
                                    static_folder=os.path.join(path, '../site/static'))
    
        self._app.add_url_rule('/', view_func=self.__home)        
        self._app.add_url_rule('/time', view_func=self.__time)
        self._app.add_url_rule('/clients', view_func=self.__clients)
        self._app.add_url_rule('/data', view_func=self.__data)
        self._app.add_url_rule('/connect', view_func=self.__connect, methods=['POST'])
        
        self._app.config['MAX_CONTENT_LENGTH'] = self._config['max_file_size_mb'] * 1024 * 1024
    

    def __clients(self):
        return str(self._clients_count), StatusCode.OK.value


    def __time(self):
        elapsed_time = time.time() - self._time
        return str(int(elapsed_time)), StatusCode.OK.value
    
    
    def __data(self):
        return self._game.get_state(), StatusCode.OK.value

    
    def __home(self):
        return render_template('index.html')
        

    def __connect(self):
        if self._clients_count == self._game.players_count:
            return self.msg("Game is full.", StatusCode.ServiceUnvaliable.value)
        
        data = request.get_json() 
        if not data:
            return self.msg('Error: Request is empty. Expected json.', StatusCode.BadRequest.value)
        
        if not data['file']:
            return self.msg('Error: Expected file.', StatusCode.BadRequest.value)
                
        if not self._game.add_client(data['metadata'], data['file']):
            return self.msg("Error adding client.", StatusCode.BadRequest.value)

        self._clients_count += 1
        if self._clients_count == self._game.players_count:
            self._process.start()
        
        return self.msg(f"""Bot has been added. Waiting for players {self._clients_count}/{self._game.players_count}.
                               Server running on: {request.root_url}""", StatusCode.OK.value)


    def __start_game(self):
        self._game.set_state()
        
        while self._game.is_playing:            
            self._game.step()             
            time.sleep(self._config['game']['delay'])
            
            
    def run(self):
        self._process = threading.Thread(target=self.__start_game, daemon=True)
        self._app.run(host=self._config['host'], port=self._config['port'], debug=self._config['debug'])
        
        
def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, default="host-config.json", help="path to host-config.json")

    return parser.parse_args()

if __name__ == "__main__":
    opt = parse_opt()
    Host(opt).run()
import argparse
import json
import threading
import signal
import time
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from flask import Flask, request

from utils.status import StatusCode
from utils.base import Base


class Platform(Base):
    def __init__(self, opt):
        super().__init__('/bothub-platform/database/logs/')
                
        try:        
            with open(opt.config, 'r') as file:
                config = json.load(file)
                self._platform_file = config['platform-file']
        except Exception as exc:
            self._is_init = False
            self.log(f'Error loading the config: {exc}', StatusCode.LoadConfigError)
            return
        
        signal.signal(signal.SIGTERM, self.__stop)
        signal.signal(signal.SIGUSR1, self.__switch_net)
        
        self._app = Flask(__name__)
    
        self._app.add_url_rule('/auth', view_func=self.__connect, methods=['POST'])
        
        self._app.config['MAX_CONTENT_LENGTH'] = self._config['max_file_size_mb'] * 1024 * 1024
        
        self._is_init = True
        self._is_run = True
        self._is_enable_net = False
        self._net_event = threading.Event()
        self._net_thread = threading.Thread(target=self.__run_net)
        
        self.log('The platform has been successfully initialized.', StatusCode.Success)
        
        
    def __del__(self):
        self.log('Finished.', StatusCode.Finished)
        
        
    def __switch_net(self, signum, frame):
        if self._is_enable_net:
            self._net_event.clear()
        else:
            self._net_event.set()
        
        self._is_enable_net != self._is_enable_net
        
    
    def __stop(self, signum, frame):
        self.is_run = False
        self.log('Stop signal', StatusCode.StopSignal)
    
    
    def __run_net(self):
        while True:
            self._net_event.wait()
            
            
    
    
    def run(self):
        if not self._is_init:
            return
        
        self._net_thread.start()
        self._net_event.clear()

        self.log('running....', StatusCode.Success)
        while self._is_run:
            self.log('some log')
            time.sleep(1)
            
    

def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, default='platform/platform-config.json', help='path to platform-config.json')

    return parser.parse_args()


if __name__ == '__main__':
    opt = parse_opt()
    Platform(opt).run()

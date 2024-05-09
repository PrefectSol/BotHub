import argparse
import json
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from utils.status import StatusCode
from utils.base import Base


class Platform(Base):
    def __init__(self, opt):
        self._is_init = True
        
        try:        
            with open(opt.config, 'r') as file:
                self._config = json.load(file)
        except Exception as _:
            self._is_init = False
            self.log('Error loading the config.', StatusCode.LoadConfigError)

        super().__init__('/bothub-platform/database/logs/')
        
        self.log('The platform has been successfully initialized.', StatusCode.Success)
        
        
    def __del__(self):
        pass
        
    
    def run(self):
        if not self._is_init:
            return
        
        
    

def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, default='platform/platform-config.json', help='path to platform-config.json')

    return parser.parse_args()


if __name__ == '__main__':
    opt = parse_opt()
    Platform(opt).run()
    
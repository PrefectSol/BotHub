import requests
import argparse
import json
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from requests.exceptions import RequestException
from hub.network_interface import NetworkInterface


class Client:
    def __init__(self, opt):
        super().__init__()
        print(f'Optional arguments: {opt}')

        try:
            with open(opt.config, 'r') as file:
                self._config = json.load(file)
        except Exception as e:
            print(f'Error loading configuration: {e}')
            return

        self._url = f"http://{self._config['host']}:{self._config['port']}/connect"
        self._headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        
        self._json = self._config['request']
        print(f'Client has been created: {self._json}')
        
        with open(self._config['request']['bot'], 'r') as file:
            self._json['file'] = file.read()
        

    def connect(self):
        try:
            response = requests.post(url=self._url, json=self._json, headers=self._headers)
            print(f"Status: {response.status_code} {json.loads(response.text)['message']}")
        except RequestException as e:
            print(f'Request Error: {e}')
        except Exception as e:
            print(f'Error: {e}')
            
def create(opt):
    manager = NetworkInterface()
    


def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, default="host-config.json", help="path to host-config.json")

    return parser.parse_args()

if __name__ == "__main__":
    opt = parse_opt()
    create(opt)

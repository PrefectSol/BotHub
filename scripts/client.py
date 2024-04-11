import requests
import argparse
import json
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from requests.exceptions import RequestException
from utils.base import Base


class Client(Base):
    def __init__(self, opt):
        super().__init__()
        self.log(f'Optional arguments: {opt}')

        try:
            with open(opt.config, 'r') as file:
                self._config = json.load(file)
        except Exception as e:
            self.log(f'Error loading configuration: {e}')
            return

        self._url = f"http://{self._config['host']}:{self._config['port']}/connect"
        self._headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        
        self._json = self._config['request']
        with open(self._config['request']['bot'], 'r') as file:
            self._json['file'] = file.read()
        
        self.log(f'Client has been created: {self._config}')


    def connect(self):
        try:
            response = requests.post(url=self._url, json=self._json, headers=self._headers)
            self.log(f"Status: {response.status_code} {json.loads(response.text)['message']}")
        except RequestException as e:
            self.log(f'Request Error: {e}')
        except Exception as e:
            self.log(f'Error: {e}')


def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, default="client-config.json", help="path to client-config.json")

    return parser.parse_args()

if __name__ == "__main__":
    opt = parse_opt()
    Client(opt).connect()

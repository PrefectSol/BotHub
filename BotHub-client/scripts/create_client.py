import argparse
import json
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from hub.network_interface import NetworkInterface
from utils.permissions import Permissions


def auth(opt) -> int:
    print(f'Optional arguments: {opt}')

    try:
        with open(opt.config, 'r') as file:
            config = json.load(file)
    except Exception as exc:
        print(f'Error loading configuration: {exc}')
        return 1
    
    try:
        api_data = NetworkInterface.generate_api_data(Permissions(config['auth']['permissions']['hostManagement'],
                                                                  config['auth']['permissions']['botManagement'],
                                                                  config['auth']['permissions']['databaseView']))
    except Exception as exc:
        print(f'Failed to create API key: {exc}')
        return 1
    
    if 'error' in api_data:
        print('Key creation error:', api_data['error'])
        return 1
    
    try:
        config['auth']['apiKey'] = api_data['apiKey']
        config['auth']['apiSecret'] = api_data['apiSecret']
    except Exception as exc:
        print(f'Failed to read API key or secret: {exc}')
        return 1
    
    with open(opt.config, 'w') as file:
        file.write(json.dumps(config, indent=4))
        
    print('The API key has been successfully written to the config.json')
        
    return 0


def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, default="client-config.json", help="path to client-config.json")

    return parser.parse_args()


if __name__ == "__main__":
    opt = parse_opt()
    exit(auth(opt))

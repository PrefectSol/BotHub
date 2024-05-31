import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from utils.permissions import Permissions

class NetworkInterface:
    def __init__(self, key, secret):
        pass
    
    
    @staticmethod
    def generate_api_data(permissions: Permissions) -> dict:
        return { 'apiKey': 'hello', 'apiSecret': 'world' }
        
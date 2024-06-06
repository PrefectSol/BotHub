import os
import time
import threading
import hashlib
import secrets
from datetime import datetime

from utils.status import StatusCode
from utils.permissions import Permissions


class Base:
    def __init__(self, base_dir: str):
        self._secret_size = 16
        self._is_update = False
        
        self._users_dir = os.path.join(base_dir, 'users/')
        self._platform_dir = os.path.join(base_dir, 'platform/')
        self._hosts_dir = os.path.join(base_dir, 'hosts/')
        
        if not os.path.exists(self._users_dir):
            os.mkdir(self._users_dir)
            
        if not os.path.exists(self._platform_dir):
            os.mkdir(self._platform_dir)
            
        if not os.path.exists(self._hosts_dir):
            os.mkdir(self._hosts_dir)
            
        self.__update_dates()
        
        self._update_thread = threading.Thread(target=self.__updater)
    

    def init_base(self, encoder):
        self._encoder = encoder
    
        
    def __update_dates(self):
        self._current_date = datetime.now()
        self._plog_file = os.path.join(self._platform_dir, self._current_date.strftime("%Y-%m-%d-%H:%M:%S"))
    

    def __updater(self):
        while self._is_update:
            elapsed_time = datetime.now() - self._current_date
            if elapsed_time.total_seconds() >= self._log_update * 3600:
                self.__update_dates()

            time.sleep(self._delay)
    
    
    def __check_user(self, user_id, user_sign, permissions: Permissions = None) -> StatusCode:
        userfile = os.path.join(self._users_dir, f'user_{user_id}.env')
        if not os.path.isfile(userfile):
            return StatusCode.UnknownUser
        
        with open(userfile, 'r') as file:
            data = file.read().split(' ')
            
        if data[0] != user_sign:
            return StatusCode.InvalidSignature
        
        if permissions != None:
            if not(data[1] == str(permissions.get_host_permission()) and data[2] == str(permissions.get_bot_permission()) and data[3] == str(permissions.get_view_permission())):
                return StatusCode.InvalidPermissions
            
        return StatusCode.Success
    
    
    def run_updater(self, log_update: float, delay: int):
        self._log_update = log_update
        self._delay = delay
        self._is_update = True
        self._update_thread.start()
        
    
    def stop_updater(self):
        self._is_update = False
        
        
    def create_host(self, user_id, user_sign, host: dict) -> tuple[int, StatusCode]:
        pass
            
    
    def delete_user(self, user_id, user_sign) -> StatusCode:
        userfile = os.path.join(self._users_dir, f'user_{user_id}.env')
        result = self.__check_user(user_id=user_id, user_sign=user_sign)
        if result == StatusCode.Success:
            os.remove(userfile)
        
        return result
     
    
    def add_user(self, permissions: Permissions) -> tuple[dict, StatusCode]:
        files = [name for name in os.listdir(self._users_dir) if os.path.isfile(os.path.join(self._users_dir, name)) and name.startswith('user_')]
        numbers = [int(file.split('_')[1].split('.')[0]) for file in files]
        user_id = str(min(set(range(1, len(numbers) + 2)) - set(numbers)))
        
        user_secret = secrets.token_hex(self._secret_size)
        
        hash_object = hashlib.sha256()
        hash_object.update((user_id + user_secret).encode(self._encoder))
        secret_hash = hash_object.hexdigest()
        
        with open(self._users_dir + f'user_{user_id}.env', 'w') as file:
            file.write(f'{secret_hash} {permissions.get_host_permission()} {permissions.get_bot_permission()} {permissions.get_view_permission()}')
            
        return {'user_id': user_id, 'user_secret': user_secret}, StatusCode.Success
    
    
    def plog(self, msg: str, status: StatusCode = StatusCode.Unknown):
        with open(self._plog_file, 'a') as file:
            file.write(f'[{datetime.now()}] --- [{status.name}:{status.value}] --- {msg}\n')
            
            
    def hlog_to(self, msg: str, target: str, status: StatusCode = StatusCode.Unknown):
        with open(os.path.join(self._hosts_dir, target), 'a') as file:
            file.write(f'[{datetime.now()}] --- [{status.name}:{status.value}] --- {msg}\n')

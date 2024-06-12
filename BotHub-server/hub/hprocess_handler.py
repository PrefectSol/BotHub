from threading import Thread
from multiprocessing import Pipe

from hub.hprocess import HProcess


class HProcessHandler:
    def __init__(self, logger):
        self._processes = {}
        self._log = logger
        
        
    def create(self, game_config: dict, source_code: str, settings: dict, host_id: int) -> int:
        parent_conn, child_conn = Pipe()
        
        hprocess = HProcess(child_conn, game_config, source_code, settings)
        hprocess.start()

        comm_thread = Thread(target=self._communicate, args=(parent_conn, child_conn, hprocess.pid, host_id))
        self._processes[host_id] = [hprocess, True]
        comm_thread.start()

        return hprocess.pid
    
    
    def delete(self, host_id):
        self._processes[host_id][0].kill()
        self._processes[host_id][0].join()
        self._processes[host_id][1] = False
    
    
    def _communicate(self, parent_conn, child_conn, pid, host_id):
        while self._processes[host_id][1]:
            data = parent_conn.recv()
            self._log(data['msg'], str(host_id), data['status'])
        
        self._processes.pop(host_id)
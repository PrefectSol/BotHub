from enum import Enum

class StatusCode(Enum):
    Continue = 100
    OK = 200
    BadRequest = 400
    Gone = 410
    ServiceUnvaliable = 503

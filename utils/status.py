from enum import Enum


class StatusCode(Enum):
    Success = 0
    LoadConfigError = 1
    

class HttpCode(Enum):
    Continue = 100
    Ok = 200
    BadRequest = 400
    Gone = 410
    ServiceUnvaliable = 503

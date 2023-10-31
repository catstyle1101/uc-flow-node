from enum import Enum

URL_API_GENERAL = 'v2api/'


class ActionEnum(str, Enum):
    authorization = 'authorization'
    customer = 'customer'

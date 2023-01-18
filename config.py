import os
from dataclasses import dataclass

PG_USER = os.getenv('PG_USER')
PG_PASS = os.getenv('PG_PASS')
PG_DB = os.getenv('PG_DB')

PG = 'postgresql://postgres:pgidgaf@127.0.0.1:6233/bank_transes'

@dataclass
class Statuses:
    NEW: str = 'New'
    PROCCESSED: str = 'In process'
    SUCCESSED: str = 'Success'
    DECLINED: str = 'Decline'
    

API_PATH = '/api/v1'

USER_INFO_PATH = f'{API_PATH}/getUser'

USER_TRANSACTION_PATH = f'{API_PATH}/send'

USER_SET_NEW = f'{API_PATH}/setUser'
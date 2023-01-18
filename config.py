import os


DATABASE = {
    'drivername': 'postgresql',
    'host': '127.0.0.1',
    'port': '6233',
    'username': os.getenv('PG_USER'),
    'password': os.getenv('PG_PASS'),
    'database': os.getenv('PG_DB')
}

API_PATH = '/api/v1'

USER_INFO_PATH = f'{API_PATH}/getUser'

USER_TRANSACTION_PATH = f'{API_PATH}/send'

USER_SET_NEW = f'{API_PATH}/setUser'
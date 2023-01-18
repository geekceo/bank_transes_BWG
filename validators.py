import alchemy
from config import Statuses

def validate_transaction_status(uname: str, amount: str):
    u_balance = alchemy.get_user_balance(uname)
    
    return Statuses.NEW if u_balance >= amount else Statuses.DECLINED
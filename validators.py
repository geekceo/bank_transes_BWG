import alchemy
from schemas import Transaction
from config import Statuses

def validate_transaction(uname: str, amount: str, withdrawal: bool = False, transaction: Transaction = None):
    u_balance = alchemy.get_user_balance(uname)
    
    status = Statuses.SUCCESSED if u_balance >= amount else Statuses.DECLINED
    
    alchemy.save_transaction(
        u_from=uname,
        u_to=transaction.u_to if not withdrawal else 'withdrawal',
        amount=amount,
        status=status
    )
    
    if status == Statuses.DECLINED:
        return status
    
    if withdrawal:
        alchemy.update_balance(
                uname=uname,
                new_balance=alchemy.get_user_balance(uname) - amount)
    else:
        for partner in [transaction.u_from, transaction.u_to]:
            alchemy.update_balance(
                uname=partner,
                new_balance=alchemy.get_user_balance(partner) - amount)
            '''To make less code - do amount negative to change minus sign to plus in upper operation'''
            amount *= -1
            
    return status
from fastapi import FastAPI, Query, Body
from schemas import User, Transaction, TransactionOut
import alchemy
import validators
import config
from config import Statuses

app = FastAPI()

'''Path to get user info via user name'''
@app.get(config.USER_INFO_PATH)
def get_user(uname: str=Query(default=None)):
    if uname is None:
        #raise 'Name Error, param uname can\'t be empty' 
        return {'error': 'param uname can\'t be empty'}
    
    data = alchemy.get_user(uname)
    
    return data

'''Path to set new user in DB'''
@app.post(config.USER_SET_NEW)
def set_user(user: User=Body(embed=True)):
    alchemy.create_user(name=user.name, balance=user.balance)
    
    return User(**user.dict())

'''Path to create new trasaction'''
@app.post(config.USER_TRANSACTION_PATH)
def transaction_send(transaction: Transaction=Body(embed=True)):
    status = validators.validate_transaction_status(uname=transaction.u_from, amount=transaction.amount)
    
    alchemy.save_transaction(
        u_from=transaction.u_from,
        u_to=transaction.u_to,
        amount=transaction.amount,
        status=status
    )
    
    if not status == Statuses.DECLINED:
        alchemy.update_balance(
            uname=transaction.u_from,
            new_balance=alchemy.get_user_balance(transaction.u_from) - transaction.amount)
        alchemy.update_balance(
            uname=transaction.u_from,
            new_balance=alchemy.get_user_balance(transaction.u_to) + transaction.amount)
    
    return TransactionOut(**transaction.dict(), status=status)


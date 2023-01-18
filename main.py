from fastapi import FastAPI, Query, Body
from schemas import User, Transaction
import alchemy
import validators
import config
from config import Statuses
import tasks

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
    alchemy.create_user(uname=user.name, balance=user.balance)
    
    return User(**user.dict())

'''Path to create new trasaction'''
@app.post(config.USER_TRANSACTION_PATH)
def transaction_send(transaction: Transaction=Body(embed=True)):
    validators.validate_transaction(
        transaction=transaction,
        uname=transaction.u_from,
        amount=transaction.amount
        )
         
    return Transaction(**transaction.dict())


'''Path to make withdrawal'''
@app.post(config.USER_WITHDRAWAL)
def transaction_withdrawal(transaction: Transaction=Body(embed=True)):
    tasks.create_task(pool='', task=f'{transaction.u_from}:{transaction.amount}', queue=transaction.u_from)
    
    return Transaction(**transaction.dict())

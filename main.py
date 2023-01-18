from fastapi import FastAPI, Query, Body
from schemas import User, Transaction
import alchemy
import config

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
    
    return {'name': user.name, 'balance': user.balance}

'''Path to create new trasaction'''
@app.post(config.USER_TRANSACTION_PATH)
def transaction_send(transaction: Transaction=Body(embed=True)):
    return {
            'from': transaction.u_from,
            'to': transaction.u_to,
            'amount': transaction.amount,
            'status': transaction.status
           }


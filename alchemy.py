import sqlalchemy as sqla
import config
from sql_schemas import users, transactions

engine = sqla.create_engine(config.PG)

def create_user(uname: str, balance: int):
    connection = engine.connect()
    query = users.insert().values(
        {
            'u_name': uname,
            'u_balance': balance
        }
    )

    connection.execute(query)
    
def get_user(uname: str):
    connection = engine.connect()
    query = sqla.select(users.columns.u_name, users.columns.u_balance).where(users.columns.u_name == uname)

    result = connection.execute(query).fetchone()
    
    return result

def get_user_balance(uname: str):
    connection = engine.connect()
    query = sqla.select(users.columns.u_balance).where(users.columns.u_name == uname)

    result = connection.execute(query).fetchone()[0]
    
    return result

def save_transaction(u_from: str, u_to: str, amount: int, status: str):
    connection = engine.connect()
    query = transactions.insert().values(
        {
            'u_from': u_from,
            'u_to': u_to,
            'amount': amount,
            'status': status
        }
    )

    connection.execute(query)

def update_balance(uname: str, new_balance: str):
    connection = engine.connect()
    query = sqla.update(users).where(users.columns.u_name == uname).values(u_balance = new_balance)
    
    connection.execute(query)

import sqlalchemy as sqla
from sqlalchemy.engine.url import URL
import config
from sql_schemas import users

#engine = sqla.create_engine(URL.create(**config.DATABASE))
engine = sqla.create_engine('postgresql://postgres:pgidgaf@127.0.0.1:6233/bank_transes')
#engine = sqla.create_engine('postgresql+psycopg2://postgres:pgidgaf@localhost:6233/bank_trans_db')

def create_user(name: str, balance: int):
    connection = engine.connect()
    query = users.insert().values(
        {
            'u_name': name,
            'u_balance': balance
        }
    )

    connection.execute(query)
    
def get_user(name: str):
    connection = engine.connect()
    query = sqla.select(users)#.where(users.columns.u_name==name)

    result = connection.execute(query).fetchone()
    
    
    
    return result



##transactions = sqla.Table('Transactions')
#
#metadata.create_all(engine)
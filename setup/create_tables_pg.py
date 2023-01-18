import sqlalchemy as sqla

engine = sqla.create_engine('postgresql://postgres:pgidgaf@127.0.0.1:6233/postgres')

metadata = sqla.MetaData()

users = sqla.Table('Users', metadata,
    sqla.Column('id', sqla.Integer, primary_key=True),
    sqla.Column('u_name', sqla.String),
    sqla.Column('u_balance', sqla.Integer)
)

transactions = sqla.Table('Transactions', metadata,
    sqla.Column('id', sqla.Integer, primary_key=True),
    sqla.Column('u_from', sqla.String),
    sqla.Column('u_to', sqla.String),
    sqla.Column('amount', sqla.Integer),
    sqla.Column('status', sqla.String),
)

metadata.create_all(engine)

import sqlalchemy as sqla

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

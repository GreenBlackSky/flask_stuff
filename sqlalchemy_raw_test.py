from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, MetaData


connection_data = {
    'type': 'postgres',
    'user': 'john',
    'password': 'qwerty',
    'host': 'localhost',
    'port': '5432',
    'database': 'test'
}


db = create_engine("{type}://{user}:{password}@{host}:{port}/{database}".format(**connection_data))
meta = MetaData(db)
test_table = Table('relatives', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('father_id', Integer),
    Column('mother_id', Integer)
)

with db.connect() as connection:
    test_table.create()
    query = test_table.insert().values(father_id=10, mother_id=11)
    connection.execute(query)




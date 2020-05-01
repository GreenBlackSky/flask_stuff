from sqlalchemy import create_engine
from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


connection_data = {
    'type': 'postgres',
    'user': 'john',
    'password': 'qwerty',
    'host': 'localhost',
    'port': '5432',
    'database': 'test'
}


db = create_engine("{type}://{user}:{password}@{host}:{port}/{database}".format(**connection_data))
base = declarative_base()


class User(base):
    __tablename__ = 'users'
    user_id = Column('id', Integer, primary_key=True, autoincrement=True)
    father_id = Column('father_id', Integer)
    mother_id = Column('mother_id', Integer)


base.metadata.create_all(db)


session = sessionmaker(db)()


john = User(father_id=10, mother_id=11)
session.add(john)
session.commit()

import requests
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker, mapper
from sqlalchemy.ext.declarative import declarative_base



engine = create_engine("postgres+psycopg2://cs162_user:cs162_password@192.168.99.100:5432/cs162")

class Bookmarks(object):
    pass

Base = declarative_base()


Session = sessionmaker(bind=engine)

metadata = MetaData(engine)
my_expression = Table("expression",metadata, autoload=True)
mapper(Bookmarks, my_expression)

s = Session()

print(s.query(Bookmarks).all())


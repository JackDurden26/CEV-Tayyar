from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String
import psycopg2
import random
from faker import Faker
from faker.providers import BaseProvider
import itertools

f = Faker('tr_TR')

engine = create_engine('postgresql://postgres:tayyarco@localhost:5432/postgres')

session = sessionmaker(bind = engine)()

Base = declarative_base()

class logins(Base):
    __tablename__ = 'login_tablosu'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key = True)
    email = Column(String(50),)
    password = Column(String(50))


def kayıt():
    email_full = []
    password_full = []
    for _ in range(1):
      email_full.append(f.email())
      password_full.append(f.password())

    person = logins(email = email_full[0], password = password_full[0])
    session.add(person)

num = 100
for _ in itertools.repeat(0, num):
    kayıt()
session.commit()

# class logins2(Base):
#     __tablename__ = 'login_tablosu2'
#     __table_args__ = {'extend_existing': True}
#
#     id = Column(Integer, primary_key = True)
#     email = Column(String(50),)
#     password = Column(String(50))
#
#
# n_email_full = []
# for _ in email_full[0,10]:
#     n_email_full.append(_)
#
# n_password_full = []
# for _ in password_full(0,100):
#     n_password_full.append(_)
#
# persona = logins2(email = n_email_full[0], password = n_password_full[0])
# session.add(persona)
#



Base.metadata.create_all(engine)
session.commit()




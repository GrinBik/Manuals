# Создать 5 новых строк в БД с помощью создания экземпляров класса.
# Создать ещё один класс Enemies и вписать несколько строк данных.
import random
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, DOUBLE_PRECISION, TEXT, String, FLOAT
from sqlalchemy.orm import sessionmaker


engine = create_engine("postgresql+psycopg2://postgres:hcS3tm7ro4mZb8@localhost/Rebotica")

Base = declarative_base()


class Test(Base):
    __tablename__ = 'test'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(TEXT, nullable=False)
    hp = Column(DOUBLE_PRECISION, nullable=False, default=100)
    dmg = Column(DOUBLE_PRECISION, nullable=False, default=0)


class Cats(Base):
    __tablename__ = 'Cats'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(TEXT, nullable=False)
    color = Column(String, nullable=False)


class Enemies(Base):
    __tablename__ = 'Enemies'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(TEXT, nullable=False)
    hp = Column(FLOAT, nullable=False, default=100)
    dmg = Column(FLOAT, nullable=False, default=0)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

s = Session()

for i in range(6, 11):
    s.merge(Test(id=i, name=f'name {i}', dmg=random.randint(0, 15)))

for i in range(5):
    s.merge(Enemies(id=(i+1), name=f'name {i}'))

s.commit()

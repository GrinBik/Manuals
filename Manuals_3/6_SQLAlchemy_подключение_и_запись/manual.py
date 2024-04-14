import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, DOUBLE_PRECISION, TEXT, String
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


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

s = Session()

hero = Test(id=5, name='Herc', dmg=11)
# s.add(hero)
s.merge(hero)
s.commit()

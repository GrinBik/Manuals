# 1. Удалить все строки с id больше 200. Для этого не нужен цикл, просто использовать функцию удаления
# и задать правильное условие.
# 2. Обновить имена всех строк с чётным id на “Jackie Chan”.
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, DOUBLE_PRECISION, TEXT
from sqlalchemy.orm import sessionmaker


engine = create_engine("postgresql+psycopg2://postgres:hcS3tm7ro4mZb8@localhost/Rebotica")

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(TEXT, nullable=False)
    hp = Column(DOUBLE_PRECISION, nullable=False, default=100)
    dmg = Column(DOUBLE_PRECISION, nullable=False, default=0)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
s = Session()

# задание (1)
# s.query(Users).filter(Users.id > 200).delete()
# s.commit()

# задание (2)
s.query(Users).filter(Users.id % 2 == 0).update({"name": "Jackie Chan"})
s.commit()

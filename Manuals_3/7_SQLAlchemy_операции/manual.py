import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, DOUBLE_PRECISION, TEXT
from sqlalchemy.orm import sessionmaker
import random
import faker


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

fake = faker.Faker('ru_RU')

# for i in range(400):
#     user_id = i
#     name = fake.first_name()
#     hp = 100
#     dmg = random.randint(1,12)
#     obj = Users(id=user_id, name=name, hp=hp, dmg=dmg)
#     s.merge(obj)
#     s.commit()

# data = s.query(Users).all()
# for user in data:
#     print(user.name)

# data = s.query(Users).filter(Users.dmg >= 10, Users.dmg < 12)
# for user in data:
#     print(f'id: {user.id}, name: {user.name}, dmg: {user.dmg}')

# s.query(Users).filter(Users.id == 1).update({"name": "Lee"})
# s.commit()

s.query(Users).filter(Users.id == 0).delete()
s.commit()

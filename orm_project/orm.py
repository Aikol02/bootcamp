from requests.sessions import Session, session
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from main import main 

engine = create_engine('postgresql+psycopg2://aikol:1@localhost:5432/deputy_db')
print('Connected!!!')

Base = declarative_base()

class Deputy(Base):
    __tablename__ = 'deputy'
    id = Column(Integer, primary_key=True)
    fullname = Column(String)
    fraction = Column(String)
    telephone = Column(String)

    def __init__(self, fullname, fraction, telephone):
        self.fullname = fullname
        self.fraction = fraction
        self.telephone = telephone

    def __str__(self):
        return f'{self.fullname}, {self.fraction}, {self.telephone}'


# Base.metadata.create_all(engine)
# print('Table Created!!!')

Session =  sessionmaker(bind=engine)
session = Session()

# deputy1 = session.query(Deputy).get(1)
# print(deputy1)
# deputy1.fullname = 'Kani'
# session.commit()
# print(deputy1)

birbolovci = session.query(Deputy).filter(Deputy.fraction.ilike('%бир бол%'))

for dep in birbolovci:
    print(dep)

# data = main()
# for deputy in data:
#     session.add(Deputy(*deputy))
#     print('Successfully added zapis!')
#     session.commit()










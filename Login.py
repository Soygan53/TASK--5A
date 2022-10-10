from sqlalchemy import Column,ForeignKey,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base= declarative_base()

class FAKER(Base):

    __tablename__='Login'

    sira = Column(Integer,primary_key=True)
    E_Mail_Adresses=Column(String(100))
    Passwords=Column(String(100))

engine=create_engine("postgresql://postgres:postgres@localhost:5432/postgres")

Base.metadata.create_all(engine)

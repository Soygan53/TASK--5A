from requests import session
from Login import FAKER,Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import pandas as pd
from faker import Faker
import psycopg2
faker=Faker()
conn_string = 'postgresql://postgres:postgres@localhost:5432/postgres'
engine=create_engine("postgresql://postgres:postgres@localhost:5432/postgres")
Base.metadata.bind=engine
conn = engine.connect()
e_mail_adresses=[]
for i in range(10000):
    e_mail_adresses.append(faker.email())
    
passwords=[]
for i in range(10000):
    passwords.append(faker.password())
    
df1 = pd.DataFrame(passwords, columns =['Passwords'])
df2=pd.DataFrame(e_mail_adresses, columns =['E_Mail_Adresses'])
new_df= pd.concat([df2,df1],axis=1)

DBSession =sessionmaker(bind=engine)
session=DBSession()


new_df.to_sql('data', con=conn, if_exists='replace',
          index=False)
conn = psycopg2.connect(conn_string
                        )
conn.autocommit = True
cursor = conn.cursor()
  
sql1 = '''select * from data;'''
cursor.execute(sql1)
for i in cursor.fetchall():
    print(i)
  
# conn.commit()
conn.close()
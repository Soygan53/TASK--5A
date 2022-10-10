#!/usr/bin/env python
# coding: utf-8

# In[87]:


from faker import Faker
faker=Faker()

e_mail_adresses=[]
for i in range(10000):
    e_mail_adresses.append(faker.email())
    
passwords=[]
for i in range(10000):
    passwords.append(faker.password())
    
df1 = pd.DataFrame(passwords, columns =['Passwords'])
df2=pd.DataFrame(e_mail_adresses, columns =['E-Mail Adresses'])

pd.options.display.max_rows = 10000
pd.options.display.max_columns = 10000
pd.concat([df2,df1],axis=1)


# In[ ]:





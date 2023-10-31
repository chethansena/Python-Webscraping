#!/usr/bin/env python
# coding: utf-8

# In[16]:


import  requests
import pandas as pd 
from bs4 import BeautifulSoup

name_list= []
price_list=[]
desc_list = []
review_list = []

url='https://www.airbnb.co.in/s/Bengaluru--India/homes?adults=1&place_id=ChIJbU60yXAWrjsR4E9-UejD3_g&refinement_paths%5B%5D=%2Fhomes&checkin=2023-10-31&checkout=2023-11-04'
r= requests.get(url)
print(r)

soup = BeautifulSoup(r.text, 'lxml')
# print(soup)

for i in range(1,14):
    np = soup.find('a', class_='l1ovpqvx c1ytbx3a dir dir-ltr').get('href')
    # # print(np)

    cnp = "https://www.airbnb.co.in"+np
    print(cnp)


    name = soup.find_all('div', class_='t1jojoys dir dir-ltr')
    for i in name:
        names = i.text
        name_list.append(names)

    print(len(name_list))
    price = soup.find_all('div', class_="_1jo4hgw")
    for i in price:
        prices = i.text
        price_list.append(prices)

    print(len(price_list))

#     desc = soup.find_all('span', class_ = 't1jojoys dir dir-ltr')
#     for i in desc:
#         descs = i.text
#         desc_list.append(descs)

#     print(len(desc_list))



    # review = soup.find_all('span', class_='r1dxllyb dir dir-ltr')
    # for i in review:
    #     reviews=i.text
    #     review_list.append(reviews)

    # print(len(review_list))

df = pd.DataFrame({'Name':name_list, 'Price/Night':price_list})
print(df)

df.to_csv('AirBnB_real.csv')


# In[ ]:





# In[ ]:





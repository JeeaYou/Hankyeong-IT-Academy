#!/usr/bin/env python
# coding: utf-8

# In[6]:


def connect(검색어,cnt=1):
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    import time
    import warnings
    warnings.filterwarnings('ignore')
    # url = 이미지 url
    # urllib.request.urlretrieve(url, '파일 이름')

    url='https://search.naver.com/search.naver?where=image&sm=tab_jum&query='+검색어

    driver=webdriver.Chrome('./chromedriver.exe')
    driver.get(url)
    time.sleep(2)

    for i in range(cnt):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(2)
    html=driver.page_source

    driver.close()
    driver.quit()
    return html
    
def naver(검색어,cnt=1):
    from bs4 import BeautifulSoup as bs
    import urllib.request
    import os
    import time
    
    soup=bs(connect(검색어,cnt),'html.parser')
    elems=soup.find_all('img','_image _listImage')
    imgs=[]
    for elem in elems:
        imgs.append(elem['src'])

    os.makedirs(검색어,exist_ok=True)
    for idx,img in enumerate(res):
        urllib.request.urlretrieve(img, f'./{검색어}/{검색어}_google_{idx}.jpg')

    return


# In[ ]:





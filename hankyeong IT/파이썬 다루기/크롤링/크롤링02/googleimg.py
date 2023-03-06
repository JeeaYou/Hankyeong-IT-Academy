#!/usr/bin/env python
# coding: utf-8

# In[30]:


def connect(검색어,cnt=1):
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    import time
    # url = 이미지 url
    # urllib.request.urlretrieve(url, '파일 이름')

    url='https://www.google.com/search?q='+검색어+'&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi3jJD8xb35AhWWAN4KHYSLCaMQ_AUoAXoECAEQBA&biw=790&bih=710&dpr=1.25'
    driver=webdriver.Chrome('./chromedriver.exe')
    driver.get(url)
    time.sleep(2)
    
    for j in range(cnt):
        for i in range(5):
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            time.sleep(2)
            try:
                driver.find_element(By.XPATH,'//*[@id="islmp"]/div/div/div/div[1]/div[2]/div[2]/input').click()
                time.sleep(2)
            except:
                pass

    html=driver.page_source
    driver.close()
    driver.quit()
    
    return html

# 2. 구글 모듈화(함수)

def ggImage(검색어,cnt=1):
    '''
    ggImage(검색어,cnt=1)
    cnt는 결과 더보기를 누르는 애다 
    '''
    from bs4 import BeautifulSoup as bs
    import os
    import urllib.request
    soup=bs(connect(검색어,cnt),'html.parser')
    imgs=soup.find_all('img','rg_i Q4LuWd')
    res=[]
    for i in imgs:
        try:
            res.append(i['src'])
        except:
            res.append(i['data-src'])
            
    if os.path.exists('./'+검색어)==False:
        os.mkdir(f'{검색어}')

    #dateName = time.strftime("%Y%m%d-%H%M%S")
    for idx,img in enumerate(res):
        urllib.request.urlretrieve(img, f'./{검색어}/{검색어}_google_{idx}.jpg')
    
    return


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[57]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import pandas as pd
import time
from bs4 import BeautifulSoup as bs
import warnings
warnings.filterwarnings('ignore')

def connect(검색어,pages=1):
    htmls=[]
    # 옵션 생성
    options = webdriver.ChromeOptions()
    # 창 숨기는 옵션 추가
    options.add_argument("headless")
    
    
    for page in range(1,pages+1):
        url='https://section.blog.naver.com/Search/Post.naver?pageNo='+str(page)+'&rangeType=ALL&orderBy=sim&keyword='+검색어

        driver=webdriver.Chrome('./chromedriver.exe')
        driver.get(url)
        time.sleep(3)
        htmls.append(driver.page_source)

    driver.close()
    driver.quit()
    return htmls

def nBlog(검색어,pages=1):
    
        # 옵션 생성
    options = webdriver.ChromeOptions()
    # 창 숨기는 옵션 추가
    options.add_argument("headless")  
    
    htmls=connect(검색어,pages)
    res=[]
    for html in htmls:
        soup=bs(html,'html.parser')
        div_tags=soup.select('div.info_post')
        for  div in div_tags:
            title=div.find('span','title').text
            link=div.find('a','desc_inner')['href']
            cont=div.find('a','text').text
            writer=div.find('em','name_author').text
            date=div.find('span','date').text
            tmp={
                '제목':title,
                '작성자':writer,
                '작성일':date,
                '요약글':cont,
                '링크':link
            }
            res.append(tmp)
    df=pd.DataFrame(res)
   
    driver=webdriver.Chrome('./chromedriver.exe')
    cont_res=[]
    for i in df['링크']:
        driver.get(i)
        time.sleep(2)
        
        iframe=driver.find_element(By.ID,'mainFrame')
        driver.switch_to.frame(iframe) #irame 창으로 이동함
        
        contents=driver.find_element(By.CLASS_NAME,'se-main-container').text.replace('\n','')
        cont_res.append(contents)

    driver.close()
    driver.quit()

    df['내용']=cont_res
    print('--------------end----------------')
    return df



if __name__=='__main__':
    df_star=nBlog('스타벅스',2)
    display(df_star)


# In[ ]:





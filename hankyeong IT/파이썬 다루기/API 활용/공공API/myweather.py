#!/usr/bin/env python
# coding: utf-8

# In[9]:


import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import json

def connect(s_date,e_date,code):
    인증키="Jid5jJfVfwuc7brfbSDE6yxusvhmIOTMmmZE%2F%2F%2B2YdeSPIAoRpSnof9qpb5OSeEpyvP8xnb6AO4V7kXVEJFPEQ%3D%3D"
    시작일=s_date
    종료일=e_date
    지점코드=code
    url = "http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList?serviceKey="
    url = url + 인증키
    url = url + "&pageNo=1&dataCd=ASOS&dateCd=DAY&dataType=JSON"
    url = url + "&numOfRows=999"
    url = url + "&startDt=" + str(시작일) + "&endDt=" + str(종료일)
    url = url + "&stnIds=" + str(지점코드)

    response=requests.get(url)
    
    return response
    
#층정 지점 코드 확인
def find_code(name='서울'):
    try:
        df_code=pd.read_csv('./기상청_지역코드.csv',encoding='cp949')
        code=int(df_code[df_code['지점명']==name]['지점'])
    except:
        print('해당지역이 없습니다')
        return
    else:
        return code
  
    
    
def get_weather(s_date,e_date,code):
    f_code=find_code(code)
    if f_code==None:
        return
    
    response=connect(s_date,e_date,f_code)
    
    json_obj=json.loads(response.text)

    items=json_obj['response']['body']['items']['item']

    df=pd.DataFrame(items)
    
    df1=df[['stnNm', 'tm', 'avgTa', 'minTa', 'maxTa', 'sumRn', 'maxWs', 'avgWs']]
    df1.columns=['지점명', '일시', '평균기온', '최저기온', '최고기온', '일일강수량', '최대풍속', '평균풍속']
    return df1

if __name__=='__main__':
    data=get_weather(20220101,20220601,'속초')
    display(data)


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pickle
from collections import Counter
from konlpy.tag import Okt
import re
import os

okt=Okt()

data = pd.read_csv('../data/최종_전세사기_all_.csv') #원본 데이터
#tf불러오기
with open('../data/title_tf_df.pickle', 'rb') as f:
    tf = pickle.load(f)
#idf불러오기
with open('../data/title_idf.pickle', 'rb') as f:
    idf = pickle.load(f)
#tfidf불러오기
with open('../data/title_tfidf_df.pickle', 'rb') as f:
    tfidf = pickle.load(f)
    
class Similarity():
   
    def __init__(self,new_text):
        self.new_text=new_text

    def view_similarity3(self):
        # 새로운 글 명사 추출 후 TF구하기
        self.new_nouns=okt.nouns(self.new_text) # new_text 명사추출
        self.new_tf=pd.Series(Counter(self.new_nouns)) # new_text TF구하기
        self.new_text_filter=[i for i in self.new_tf.index if i in idf.index] # 새로 생긴 단어(idf에 없는 단어) 없애기
        self.new_tf=self.new_tf[self.new_text_filter]
        # 새로운 글 tfidf구하기
        self.new_tfidf=self.new_tf*idf
        self.new_tfidf=self.new_tfidf.fillna(0)
        self.new_tfidf=self.new_tfidf.values.reshape(1,-1)

        # 새로운 글과 가장 유사한 원본데이터(data)의 행 찾기
        self.sim_res=[cosine_similarity(self.new_tfidf,tfidf.loc[i].values.reshape(1,-1)).flatten().tolist() for i in tfidf.index]
        self.sim_res_dict=[(idx,i[0]) for idx, i in enumerate(self.sim_res)]
        self.sim10_sort=sorted(self.sim_res_dict, key=lambda x: x[1], reverse=True)[:10] # 유사한 문서 10개 (행번호,코사인유사도 값)
        self.sim10_sort_index=[i[0] for i in self.sim10_sort] #  유사한 행번호 10개, 내림차순 정렬
        self.sim10_sort_score=[i[1] for i in self.sim10_sort] #  유사도 점수 10개, 내림차순 정렬
        #저장
        filename=' '.join(re.findall('[가-힣0-9a-zA-Z]+',self.new_text)) #파일이름(한글,숫자, 영어)로 제한, 특수문자 제외
        data.iloc[self.sim10_sort_index].to_csv(f'similarity10_{filename}.csv')
        print(f'"{os.getcwd()}"폴더에 유사한 글 10개가 "{filename}.csv" 파일명으로 저장되었습니다.')
        
        # 새로운글과 유사한 문장 3개 보여주기
        self.df=data.loc[self.sim10_sort_index]
        print('==============================================================================================')
        print(f'   >>> 질문(Q) : {self.new_text}')
        print('==============================================================================================')
        for idx,i in enumerate(self.df.index[:3]):
            self.date=self.df['날짜'][i]
            print(f'\n▶ 제목({idx+1}): 유사도({self.sim10_sort_score[idx]}), <날짜:{self.date}>')
            print(self.df['title'][i])
            print(f'\n▶ 내용({idx+1}):')
            print(self.df['내용'][i])
            print(f'\n▶ 응답({idx+1}):')
            print(self.df['내용1(응답)'][i])
            print('-'*100)
        
if __name__=='__main__':
    Q='갭투자 사기 당한 것 같아요'
    s_text=Similarity(Q)
    s_text.view_similarity3()
    






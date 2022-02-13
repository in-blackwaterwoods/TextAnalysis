# -*- coding: utf-8 -*-
"""Title_NLP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12-66QTcUdJF0uLghrnfT_6kZSbl4uRPr
"""

#분석할 텍스트 데이터 불러오기 
import pandas as pd
df = pd.read_csv('/content/sunscreen_title.csv', encoding='utf-8')
df[0:146]

txt = df["제목"].to_list()

#필요한 패키지 설치 
! apt-get install g++ openjdk-8-jdk python3-dev python3-pip curl
! python3 -m pip install --upgrade pip
! python3 -m pip install konlpy

##텍스트 토큰화 

from nltk import sent_tokenize 
import nltk 

nltk.download('punkt')

sentences = [] 
for i in range(0,146):  
  sentence = sent_tokenize(text=txt[i])
  sentences.extend(sentence)

print(sentences)
len(sentences)

from nltk import word_tokenize 

words = [] 

for i in sentences:
  word = word_tokenize(i)
  words.extend(word)

print(words)

len(words)

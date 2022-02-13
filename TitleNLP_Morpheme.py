# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AJKBkrD5z6RC_5TTvCrffkZsD61p01YH

# **2. 형태소 분석하기**
"""

##명사 추출 
from konlpy.tag import Okt
import numpy as np
okt = Okt()


clean_nouns = []

for k in words_list:
  nouns = okt.nouns(k)

  for noun in nouns:
    clean_nouns.append(noun)

print(clean_nouns)
len(clean_nouns)

# 만들어진 리스트 텍스트 파일로 저장 
for i in clean_nouns:
  f = open('clean_nouns.txt','a', encoding= 'utf8')
  f.write(i+ '\n')
  f.close()

from konlpy.tag import Okt
import numpy as np
okt = Okt()

#동사/부사/형용사 추출 
clean_verbs = []

for j, tag in enumerate(words_list):
  for word in okt.pos(tag, stem=True):      #어근 
    if word[1] in ['Hashtag']:
      clean_verbs.append(word[0])
      print(word[0])
print(clean_verbs)

# 만들어진 리스트 텍스트 파일로 저장 
for i in clean_verbs:
  f = open('clean_hashtags.txt','a', encoding= 'utf8')
  f.write(i+ '\n')
  f.close()
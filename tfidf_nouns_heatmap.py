#!/usr/bin/env python
# coding: utf-8

# In[64]:


import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
from matplotlib import font_manager, rc



# In[65]:


df = pd.read_csv('tfidf_nouns.csv', index_col='Product', encoding='utf-8')
df


# In[89]:



sns.heatmap(data=df, vmax = 1, vmin = 0, center = 0.2, annot=False, linecolor='black', linewidths=1, cmap = 'coolwarm')
sns.set(rc={'figure.figsize': (11.7,8.27)})

plt.rcParams["axes.unicode_minus"] = False
path = "C:/Windows/Fonts/NanumGothicExtraBold.ttf"
font_name = font_manager.FontProperties(fname=path).get_name()

plt.savefig('C:/Users/hjo3o/Desktop/textm/data/StoryText_Analysis/output_figure.png',dpi=600)
rc("font", family=font_name)
plt.show()



#plt.figure(figsize=(20,20))
#plt.xticks(size=12)
#plt.yticks(size=12, rotation=0)


print('資料為參考,若有相關戶政問題以政府回應為主')
print('4-進行兩問題相似性的評估')
import jieba
jieba.set_dictionary('dict.txt.big')
import pandas as pd
from numpy.linalg import norm
import response3
import numpy as np
df = response3.df
all_terms = response3.all_terms
idf_vector = response3.idf_vector
termindex = response3.termindex
print('準備評估兩問題')
def cosine_similarity(vector1, vector2):
    score = np.dot(vector1, vector2)/(norm(vector1)*norm(vector2))
    return score
print('開始找兩個問題出來')
sentence1 = df.loc[0]
sentence2 = df.loc[35]
sentence3 = df.loc[1]
print(sentence1['question'])
print(sentence2['question'])
print(sentence3['question'])
cos1 = cosine_similarity(sentence1['vector'], sentence2['vector']) #要拿轉換後的值下去分析
print(cos1)
cos2 = cosine_similarity(sentence1['vector'], sentence3['vector'])
print(cos2) #同為育兒津貼之問題相似度較高

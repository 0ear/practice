print('資料為參考,若有相關戶政問題以政府回應為主')
print('3-進行tf idf計算')
import jieba
jieba.set_dictionary('dict.txt.big')
import pandas as pd
import response2
import numpy as np
df = response2.df
all_terms = response2.all_terms
idf_vector = response2.idf_vector
termindex = response2.termindex
print('tf推算後取得tfidf的結果')
def terms_to_vector(terms):
    #print('先規劃一空向量')
    vector = np.zeros_like(termindex, dtype = np.float32)
    for term in terms:
        idx = termindex.index(term)
        vector[idx] += 1
    vector = vector*idf_vector
    return vector
df['vector'] = df['processed'].apply(terms_to_vector)
html=df.to_html()
with open('response2.html', 'w', encoding = 'utf-8-sig') as file:
    file.writelines('<meta charset = "UTF-8">\n')
    file.write(html)

print('資料為參考,若有相關戶政問題以政府回應為主')
print('2-進行idf計算')
import jieba
print('進行分詞及了解資料')
jieba.set_dictionary('dict.txt.big')
import pandas as pd
import response
import numpy as np
df = response.df
all_terms = response.all_terms
print(len(all_terms))
print(all_terms)  #發現有重複的詞彙
print('要取沒有重複的資料，因此透過set()來實現')
termindex = list(set(all_terms))
print(len(termindex))
print(termindex)
print('要進行tf idf計算,先了解有多少個字串')
doc_length = len(df)
idf_vector = []
for term in termindex:
    num_of_doc_contrains_term = 0
    for terms in df['processed']:
        if term in terms:
            num_of_doc_contrains_term += 1
    idf = np.log(doc_length/num_of_doc_contrains_term)
    idf_vector.append(idf)
print(len(idf_vector))
print(idf_vector)
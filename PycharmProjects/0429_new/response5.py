print('資料為參考,若有相關戶政問題以政府回應為主')
print('5-使用者輸入資料後回應')
import jieba
jieba.set_dictionary('dict.txt.big')
import pandas as pd
from numpy.linalg import norm
import response3, response, response4
import numpy as np
df = response4.df
def retrieve(testing_sentence, return_num = 3):
    print('針對t使用者輸入的資料進行轉換')
    testing_vector = response3.terms_to_vector(response.preprocess(testing_sentence))
    score_dict = {}
    print('進行相似度查找')
    for idx, vec in enumerate(df['vector']):
        score = response4.cosine_similarity(testing_vector, vec)
        score_dict[idx] = score
    idxs = np.array(sorted(score_dict.items(), key = lambda x:x[1], reverse = True))[:return_num, 0]
    return idxs
query = input('請輸入你的問題')
q1 = retrieve(query)
for x in q1:
    print('相似問題')
    print(df.loc[x, 'question'])
    print('回答')
    print(df.loc[x, 'ans'])
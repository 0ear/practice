print('資料為參考,若有相關戶政問題以政府回應為主')
import jieba
print('進行分詞及了解資料')
jieba.set_dictionary('dict.txt.big')
import pandas as pd
df = pd.read_csv('df1.csv', encoding = 'utf-8-sig')#為中文檔案要留意編碼部分
#print(df.head())
print(df.shape)
df.columns = ['question', 'ans']
html = df.to_html()
with open('response.html', 'w', encoding = 'utf-8-sig') as file:
    file.writelines('<meta charset = "UTF-8">\n')
    file.write(html)
print('進行分詞')
all_terms = []
def preprocess(item):
    terms = [t for t in jieba.cut(item, cut_all = True)]
    all_terms.extend(terms)
    return terms
df['processed'] = df['question'].apply(preprocess)
html=df.to_html()
with open('response2.html', 'w', encoding = 'utf-8-sig') as file:
    file.writelines('<meta charset = "UTF-8">\n')
    file.write(html)
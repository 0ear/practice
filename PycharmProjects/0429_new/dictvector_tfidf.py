from sklearn.feature_extraction.text import CountVectorizer
corpus = [
    'This is the first document.',
    'this document is the second document.',
    'And this is the third one.',
    'Is this the first document?',
]
vectorizer = CountVectorizer()
#vectorizer = CountVectorizer(lowercase = False) #區分大小寫用
X = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names())
print(X)
print()
print(X.toarray())
from sklearn.feature_extraction.text import TfidfTransformer
transformer = TfidfTransformer()
tfidf = transformer.fit_transform(X)
print(tfidf.toarray()) #顯示詞彙出現頻率
print('針對tfidf的其他處理方式')
from sklearn.metrics.pairwise import cosine_similarity
print(cosine_similarity(tfidf[-1], tfidf, dense_output=False))
print()
print(cosine_similarity(tfidf[-1], tfidf))
print()
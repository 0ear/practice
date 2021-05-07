from sklearn.feature_extraction.text import CountVectorizer
corpus = [
    'This is the first document.',
    'this document is the second document.',
    'And this is the third one.',
    'Is this the first document?',
]
#vectorizer = CountVectorizer()
vectorizer = CountVectorizer(lowercase = False) #區分大小寫用
X = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names())
print(X)
print()
print(X.toarray())
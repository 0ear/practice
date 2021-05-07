measurements = [{'city': 'Taipei', 'tempature':26},
                {'city': 'Taichung', 'tempature':28},
                {'city': 'Kaohsiung', 'tempature':30}]
from sklearn.feature_extraction import DictVectorizer
vec = DictVectorizer()
print(vec.fit_transform(measurements).toarray())
print(vec.get_feature_names())

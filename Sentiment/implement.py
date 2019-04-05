__author__ = 'Harsh Patel'

import pickle
from sklearn.feature_extraction.text import CountVectorizer

file=open("reviews_train_clean","rb")
reviews_train_clean=pickle.load(file)
file.close()
print('start')
cv = CountVectorizer(binary=True)
cv.fit(reviews_train_clean)
print('fit')

list=['yes','not at all']
print(len(list))
list=cv.transform(list)

filename="finalized_model.sav"
final_model = pickle.load(open(filename, 'rb'))
print(final_model.predict(list))

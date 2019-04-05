__author__ = 'Harsh Patel'

import re

#step 1
reviews_train = []
for line in open('aclImdb/movie_data/full_train.txt', 'r'):
    reviews_train.append(line.strip())

reviews_test = []
for line in open('aclImdb/movie_data/full_test.txt', 'r'):
    reviews_test.append(line.strip())


#step 2
REPLACE_NO_SPACE = re.compile("(\.)|(\;)|(\:)|(\!)|(\')|(\?)|(\,)|(\")|(\()|(\))|(\[)|(\])")
REPLACE_WITH_SPACE = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)")

def preprocess_reviews(reviews):
    reviews = [REPLACE_NO_SPACE.sub("", line.lower()) for line in reviews]
    reviews = [REPLACE_WITH_SPACE.sub(" ", line) for line in reviews]

    return reviews

reviews_train_clean = preprocess_reviews(reviews_train)
reviews_test_clean = preprocess_reviews(reviews_test)

import pickle

file=open("reviews_train_clean","wb")
pickle.dump(reviews_train_clean,file)
file.close()
file=open("reviews_test_clean","wb")
pickle.dump(reviews_test_clean,file)
file.close()

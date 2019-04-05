__author__ = 'Harsh Patel'

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pickle

file=open("reviews_train_clean","rb")
reviews_train_clean=pickle.load(file)
file.close()
file=open("reviews_test_clean","rb")
reviews_test_clean=pickle.load(file)
file.close()


cv = CountVectorizer(binary=True)
cv.fit(reviews_train_clean)


X = cv.transform(reviews_train_clean)
X_test = cv.transform(reviews_test_clean)
print(X[:10])
target = [1 if i < 12500 else 0 for i in range(25000)]
print(target[0:5])
# X_train, X_val, y_train, y_val = train_test_split(
#     X, target, train_size = 0.75
# )

# for c in [0.01, 0.05, 0.25, 0.5, 1]:
#
#     lr = LogisticRegression(C=c)
#     lr.fit(X_train, y_train)
#     print ("Accuracy for C=%s: %s"
#            % (c, accuracy_score(y_val, lr.predict(X_val))))

print('yes')
final_model = LogisticRegression(C=0.05)
final_model.fit(X, target)

filename = 'finalized_model.sav'
pickle.dump(final_model, open(filename,'wb'))

print(type(final_model))
print(final_model.predict(X_test))
# print ("Final Accuracy: %s"
#        % accuracy_score(target, final_model.predict(X_test)))
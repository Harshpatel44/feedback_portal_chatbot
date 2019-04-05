from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from gensim.models import Word2Vec
import numpy as np
import pickle
stop_words=set(stopwords.words("english"))        #importing stop words
# define training data
file=open('data_samples_input','rb')

a=np.zeros((100,1))
print(a.shape)

for line in pickle.load(file):           #for each line in the loaded file


    tokenizer = RegexpTokenizer(r'\w+')    #tokenizing
    words=tokenizer.tokenize(line)

    filtered_lists=[]
    for w in words:                    # removing stop words
        if(w not in stop_words):
            filtered_lists.append(w)
    sentences=[filtered_lists]
    print(sentences)

    # train model
    model = Word2Vec(sentences, min_count=1,size=5)       # applying word2vec to the sentence
    # summarize the loaded model

    # summarize vocabulary
    words = model[model.wv.vocab]
    print(words.shape)
    while words.shape[0]<100:
         words=np.append(words,[[0]],axis=0)
    words2=np.transpose(words)
    #print(words2)
    #print(words2.shape)


    print(a.shape)
    a=np.append(a,words2,axis=0)                      # appending each sentence's vector
    #print(a)
    #print(a.shape)


    #save model
    #model.save('model.bin')
    # load model
    #new_model = Word2Vec.load('model.bin')
    #input()




print(a.shape)
a = np.delete(a, (0), axis=0)           #deleting the first row
print(a.shape)
print(a[0])

np.savetxt('data_samples_vectors.out', a, delimiter=',')

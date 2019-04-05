import numpy as np
import matplotlib.pyplot as pl
import pickle
f=open("theta","rb")
theta=pickle.load(f)

X = np.loadtxt('data_samples_vectors.out',delimiter=',')

f=open("data_samples_output","rb")
y=pickle.load(f)
f.close()


def sigmoid(z):

    den = 1.0 + np.e ** (-1.0 * z)

    d = 1.0 / den
    #print(d)
    return d



y_new=[]
p=sigmoid(X.dot(theta))
print(p)
for i in p:

    if(i>=0.50):
        y_new.append([1])
    else:
        y_new.append([0])
print(y_new==y)   #checking if the predicted values match with the trained values.


def plot():
    X_plot=[]             #X_plot contains all the values for which y is 1
    Y_plot=[]
    for i in range(500):
        if(y_new[i]==[0]):
            Y_plot.append(X[i])
        if(y_new[i]==[1]):
            X_plot.append(X[i])
    X_plot=np.array(X_plot)
    Y_plot=np.array(Y_plot)
    print(X_plot.shape)
    print(Y_plot.shape)

    print(theta)
    pl.plot(X_plot[:,20],'ro')
    pl.axis([-.1,1,-.1,1])
    pl.plot(Y_plot[:,2],Y_plot[:,3],'bs')
    pl.show()

plot()
__author__ = 'Harsh Patel'


# taking data from the sample input file and creating list of input and output data sets stored using pickle.

import pickle
list=[]
list2=[]

file=open('amazon_cells_labelled.txt','r')
for line in file:
    data=file.readline()
    print(data)
    list.append(data[:-3])
    list2.append(data[-2])

print(list)
print(len(list))
print(list2)
print(len(list2))
file=open('data_samples_input','wb')
pickle.dump(list,file)
file.close()
file=open('data_samples_output','wb')
pickle.dump(list2,file)
file.close()
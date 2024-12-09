import numpy as np
f=open("facebook_combined.txt",'r')
nb_nodes=4039
A=np.zeros((nb_nodes,nb_nodes),dtype='int')
for line in f:
    [i,j]=line.split(' ')
    i,j=int(i),int(j)
    A[i,j]=A[j,i]=1

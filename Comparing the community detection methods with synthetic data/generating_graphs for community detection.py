import numpy as np 
import igraph as ig
from tqdm import tqdm
import pickle


p=0.3
fractions=np.linspace(1e-4,0.6,50)
graph_list=[]
real_partition_list=[]
n_iter=100
for fraction in tqdm(fractions):
    score=0
    graph_list.append([])
    real_partition_list.append([])
    for iter in range(n_iter):
        # Define the sizes of each block  
        block_sizes = [np.random.randint(200,501) for i in range(5)]   
        # Define the probability matrix for edges between blocks  
        nb_blocks = len(block_sizes)
        n=sum(block_sizes)
        p_matrix = [[p if i==j else p*fraction for i in range(nb_blocks)] for j in range(nb_blocks)]
        # Generate the stochastic block model graph  
        graph = ig.Graph.SBM(n=sum(block_sizes), block_sizes=block_sizes, pref_matrix=p_matrix)  
        A=np.array(graph.get_adjacency().data)
        permutation = np.random.permutation(n)
        permuted_A = A[permutation, :][:, permutation]
        graph_list[-1].append(permuted_A)
        real_partition_list[-1].append(np.array([i for i in range(len(block_sizes)) for j in range(block_sizes[i])])[permutation])
with open('graph_list.pkl', 'wb') as fichier:
    pickle.dump(graph_list, fichier)
with open('real_partition_list.pkl', 'wb') as f2:
    pickle.dump(real_partition_list, f2)


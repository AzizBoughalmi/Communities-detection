import networkx as nx
import matplotlib.pyplot as plt
import numpy as np 
import random 
import pickle


def matrice_proba(taille, min_diag=0.4, max_diag=0.6, min_off_diag=0.01, max_off_diag=0.08):
    """Cette fonction permet de générer une matrice carrée contenant les différentes probabilités que deux noeuds d'une même communauté ou 
     de deux communautés différentes soient liés
     La probabilité que deux noeuds d'une même communauté soient liés est entre [min_diag , max_diag]
     La probabilité que deux noeuds de deux communautés soient liés est entre [min_off_diag , max_off_diag]"""
    matrice = np.zeros((taille, taille))
    for i in range(taille):
        for j in range(i, taille):
            if i == j:
                # Pour la diagonale
                matrice[i, j] = np.random.uniform(min_diag, max_diag)
            else:
                # Pour les éléments hors diagonale
                valeur = np.random.uniform(min_off_diag, max_off_diag)
                # la matrice est symétrique
                matrice[i, j] = valeur
                matrice[j, i] = valeur 
    return matrice


borne_min = 100 #le nombre minimal de noeuds dans une communauté 
borne_max = 500 #le nombre maximal de noeuds dans une communauté 
k_vrai = range(2,50,2) #le nombre de communautés

graph = [] #une liste contenant les graphes SBM générés

for longueur in range (2,50,2):
    n = [random.randint(borne_min, borne_max) for _ in range(longueur)]
    matrice = matrice_proba(longueur)
    G = nx.stochastic_block_model(n, matrice, seed=42)
    graph.append(G)

with open('list_of_graphs.pkl', 'wb') as fichier:
    pickle.dump(graph, fichier)

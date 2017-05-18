import matplotlib.pyplot as plt
import networkx as nx
import random

G=nx.erdos_renyi_graph(200,0.02)

nx.set_node_attributes(G,'infected',False)

G.node[0]['infected']=True

#for node in G.nodes_iter(data=False):
#	print(G.node[node]['infected'])

for i in range(60):
	numInfected=0
	for node in G.nodes_iter(data=False):
		if (G.node[node]['infected']==False):
			for neighbor in nx.all_neighbors(G,node):
				if (G.node[neighbor]['infected']==True):
					if(random.random()<0.1):
						G.node[node]['infected']=True
	for node in G.nodes_iter(data=False):
		if(G.node[node]['infected']==True):
			numInfected += 1
	print(numInfected)

import matplotlib.pyplot as plt
import networkx as nx

G=nx.erdos_renyi_graph(10,0.15)

nx.set_node_attributes(G,'infected',False)

G.node[0]['infected']=True

for node in G.nodes_iter(data=False):
	print(G.node[node]['infected'])

for i in range(10):
	numInfected=0
	for node in G.nodes_iter(data=False):
		if (G.node[node]['infected']==False):
			numInfectedNeighbors = 0
			for neighbor in nx.all_neighbors(G,node):
				if (G.node[neighbor]['infected']==True):
					numInfectedNeighbors=numInfectedNeighbors+1
			print(numInfectedNeighbors)

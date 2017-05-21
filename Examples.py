import matplotlib.pyplot as plt
import networkx as nx
import random

#DEFINE FUNCTIONS

#Computer Colors for Graphs Based on Status
def compute_colors(G):
	colors = []
	for node in G.nodes_iter(data=False):
		if(G.node[node]['infected'] == True):
			colors += ['r']
		else:
			colors += ['g']	
	return colors

#CREATE GRAPH

#Create Erdos-Renyi Graph
G=nx.erdos_renyi_graph(200,0.02)

#Set All Nodes in G to Not Infected
nx.set_node_attributes(G,'infected',False)


#SET INITIAL CONDITION

#Set Node 0 in G to Infected
G.node[0]['infected']=True

plt.figure(figsize=(15,15))
img = 0
layout = nx.spring_layout(G)
layout.update((x*1,y*1) for x, y in layout.items())

nx.draw_networkx_edges(G, layout, arrows=False)
nx.draw_networkx_nodes(G, pos=layout, node_color=compute_colors(G), node_size=150)
plt.savefig(("%03d" % (img,)) + '.png')
plt.clf()
img += 1


#PERFORM ITERATIONS

#60 Iterations
for i in range(60):

	#Reset Infected Count to 0
	numInfected=0

	#Iterate Over Nodes in G
	for node in G.nodes_iter(data=False):

		#If not infected
		if (G.node[node]['infected']==False):
			
			#Reset Infected Neighbors to 0
			numInfectedNeighbors = 0

			#Iterate over neighbors of Node
			for neighbor in nx.all_neighbors(G,node):

				#If neighbor is infected
				if (G.node[neighbor]['infected']==True):

					#10% Chance of Node becoming infected
					if(random.random()<0.1):
						G.node[node]['infected']=True

	#Iterate over nodes in G
	for node in G.nodes_iter(data=False):
		#If node is infected increment count
		if(G.node[node]['infected']==True):
			numInfected += 1


	#Display graph
	nx.draw_networkx_edges(G, layout, arrows=False)
	nx.draw_networkx_nodes(G, pos=layout, node_color=compute_colors(G), node_size=50)

	plt.savefig(("%03d" % (img,)) + '.png')
	plt.clf()
	img += 1

	#Print Number Infected
	print(numInfected)

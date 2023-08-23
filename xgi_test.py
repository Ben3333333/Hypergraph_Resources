#######################################
#Test code for xgi library
#Takes incidence matrix from MATLAB
#converts it to a dictionary, then
#into a hypergraph and plots the output.
#Also returns the shortest paths from
#a source node.
#######################################

import xgi
import matplotlib.pyplot as plt
import matlab

hg_dict = {}        #Empyty dictionary for hypergraph initialisation

incidence = matlab.int16(b)     #Takes the MATLAB array into incidence

for j in range(incidence.size[1]):      #Iterate through each column
    node_list = []                      #Empty list for nodes in each hyperedge
    for i in range(incidence.size[0]):  #Iterate through each row
        if incidence[i][j] == 1:        #If the node is in the hyperedge there will be a 1
            node_list.append(i + 1)     #Add the node to the list, nodes ranging in value from 1 to N (not starting at 0)

        if i == (incidence.size[0]-1):  #If this is the last iteration through the rows (last node)
            hg_dict['e' + str((j+1))] = node_list   #Set the dictionary key to a hyperedge value of e1,e2,etc.

H = xgi.Hypergraph(hg_dict)             #Hypergraph initialisation

pos = xgi.drawing.layout.pairwise_spring_layout(H)      #Hypergraph node layout specification

plt.subplots(figsize=(5,5))     #Plot size
xgi.draw_hypergraph_hull(H, pos, node_size=15, node_fc='palegreen', node_labels=True, hyperedge_labels=True, radius = 0.1)      #Hypergraph drawing specification
plt.show()      #Show plot

shortest_paths = xgi.algorithms.shortest_path.single_source_shortest_path_length(H,source_node)       #Shortest path calculations from source node
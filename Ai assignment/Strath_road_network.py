import networkx as nx
import matplotlib.pyplot as plt
from classes.bfs import BfsTraverser

G = nx.Graph()
nodes=["Sports_complex","Siwaka","Ph_1_a","Ph_1_b","STC","Phase_2","J1","Mada","Phase_3","Parking_lot"]
G.add_nodes_from(nodes)
G.nodes()#confirm nodes

#Add Edges and their weights
G.add_edge("Sports_complex","Siwaka",weight="450")
G.add_edge("Siwaka","Ph_1_a",weight="10")
G.add_edge("Siwaka","Ph_1_b",weight="230")
G.add_edge("Ph_1_a","Mada",weight="850")
G.add_edge("Ph_1_a","Ph_1_b",weight="100")
G.add_edge("Ph_1_b","STC",weight="50")
G.add_edge("Ph_1_b","Phase_2",weight="112")
G.add_edge("Phase_2","J1",weight="600")
G.add_edge("J1","Mada",weight="200")
G.add_edge("STC","Phase_2",weight="50")
G.add_edge("Phase_2","Phase_3",weight="500")
G.add_edge("STC","Parking_lot",weight="250")
G.add_edge("Phase_3","Parking_lot",weight="350")
G.add_edge("Mada","Parking_lot",weight="700")

#position the nodes to resemble Nairobis map
G.nodes["Sports_complex"]['pos'] = (0, 0)
G.nodes["Siwaka"]['pos'] = (8, 32)
G.nodes["Ph_1_a"]['pos'] = (16, 12)
G.nodes["Ph_1_b"]['pos'] = (32, 28)
G.nodes["Mada"]['pos'] = (32, 4)
G.nodes["Phase_2"]['pos'] = (8, -20)
G.nodes["Phase_3"]['pos'] = (40, 0)
G.nodes["STC"]['pos'] = (44, 4)
G.nodes["J1"]['pos'] = (4, -4)
G.nodes["Parking_lot"]['pos'] = (44, -16)

#store all positions in a variable
node_pos = nx.get_node_attributes(G,'pos')
#call BFS to return set of all possible routes to the goal
route_bfs = BfsTraverser()
routes = route_bfs.BFS(G,"Sports_complex","Parking_lot")
print(route_bfs.visited)
route_list = route_bfs.visited
#color the nodes in the route_bfs
node_col = ['darkturquoise' if not node in route_list else 'peru' for node in G.nodes()]
peru_colored_edges = list(zip(route_list,route_list[1:]))
#color the edges as well
#print(peru_colored_edges)
edge_col = ['darkturquoise' if not edge in peru_colored_edges else 'peru' for edge in G.edges()]
arc_weight=nx.get_edge_attributes(G,'weight')
nx.draw_networkx(G, node_pos,node_color= node_col, node_size=450)
nx.draw_networkx_edges(G, node_pos,width=2,edge_color= edge_col)
#nx.draw_networkx_edge_labels(G, node_pos,edge_color= edge_col, edge_labels=arc_weight)

nx.draw_networkx_edge_labels(G, node_pos, edge_labels=arc_weight)
plt.axis('off')
plt.show()

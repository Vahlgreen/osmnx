import osmnx as ox
import matplotlib.pyplot as plt
import networkx as nx
import plotly.graph_objects as go
import numpy as np
import geopandas as gp


#ox.plot_graph(ox.graph_from_place('Denmark'))

graph = ox.graph_from_point((55.5733495, 12.2280125), dist=500, network_type='all',simplify=True)
#nodes, edges = ox.graph_to_gdfs(graph)
nodes = graph.nodes()
G = graph.edges
ox.plot_graph(G)
plt.show()
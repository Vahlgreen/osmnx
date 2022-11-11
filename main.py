import osmnx as ox
from IPython.display import Image
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from descartes import PolygonPatch
from shapely.geometry import MultiPolygon
from shapely.geometry import Polygon
import networkx as nx
import plotly.graph_objects as go
import numpy as np
import geopandas as gp
from matplotlib import colors

def create_cmap():
    cmap = colors.LinearSegmentedColormap.from_list(name = "reds",colors=["black","grey"])

    return cmap
def find_nodes_of_interest(G,origin,destinations):
    paths =[]
    nearest_node_origin = ox.distance.nearest_nodes(G, X=origin[1],Y=origin[0])
    for node in destinations:
        nearest_node_destination = ox.distance.nearest_nodes(G,X=node[1],Y=node[0])
        shortest_path = ox.shortest_path(G,nearest_node_origin,nearest_node_destination)
        paths.append(shortest_path)
    return paths




################# ALLE TAGS: https://wiki.openstreetmap.org/wiki/Map_features
# Define city/cities
#karlsunde landsby
#bbox= (55.5855,55.5500,12.280,12.2140)
#JKV
#bbox= (55.67457267416585,55.62366610225154, 12.572046495254302, 12.50001613228244)
#kochsgade
bbox = (55.416726979615085,55.39510946156921, 10.427714813444426, 10.358085603984769)
#VSV
bbox = (55.403784750747555,55.38769915207539, 10.3987692446584, 10.35045388367945)
#Odense
bbox = (55.42935095140317,55.35412822345382, 10.43741988458295, 10.313225743498387)
#kbh
bbox = (55.745758380777396,55.615864686720975, 12.688008841264, 12.457620001091561)
gdf = ox.geometries_from_bbox(bbox[0],bbox[1],bbox[2],bbox[3],tags={"building": True,"railway":True})
    #,"waterway": True,"amenity":True,"barrier":True,"boundary":True,"leisure":True,"natural":True,"railway":True,"route":True})




fig, ax = ox.plot_footprints(gdf, alpha=0.7, show=False,close=False,color="black",bgcolor="white")
G = ox.graph_from_bbox(bbox[0],bbox[1],bbox[2],bbox[3], network_type="all", simplify = True)


###########Nedenstående er for centralitet#######################
# convert graph to line graph so edges become nodes and vice versa
#edge_centrality = nx.closeness_centrality(nx.line_graph(G))
#nx.set_edge_attributes(G, edge_centrality, "edge_centrality")
# color edges in original graph with closeness centralities from line graph
#ec = ox.plot.get_edge_colors_by_attr(G, "edge_centrality", cmap="binary")
#fig, ax = ox.plot_graph(G, ax = ax, edge_color=ec, edge_linewidth=2, node_size=0)
#####################################################################

ox.plot_graph(G,ax=ax, node_size=0, edge_color="black", edge_linewidth=1,edge_alpha=0.5,show=False,close=False,bbox=bbox)




plt.show()



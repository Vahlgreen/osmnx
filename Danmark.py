import osmnx as ox
from osmnx import distance
from IPython.display import Image
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

def find_nodes_of_interest(G,origin,destinations):
    paths =[]
    nearest_node_origin = ox.distance.nearest_nodes(G, X=origin[1],Y=origin[0])
    for node in destinations:
        nearest_node_destination = ox.distance.nearest_nodes(G,X=node[1],Y=node[0])
        shortest_path = ox.shortest_path(G,nearest_node_origin,nearest_node_destination)
        paths.append(shortest_path)
    return paths



img_folder = "images"
extension = "png"
size = 240

# Define city/cities
place = "Denmark"
point = (55.5733495, 12.2280125) #bredde/længdegrad = lattitude/longitude


bbox_fig = (58.2361,54.2792,13.0073,7.7266)
#bbox = (55.5752,55.2050,12.4337,12.2149)

fp = f"./{img_folder}/{place}.{extension}"

G = ox.graph_from_bbox(bbox_fig[0],bbox_fig[1],bbox_fig[2],bbox_fig[3], network_type="drive", simplify = True)
#G = ox.graph_from_place(place, network_type="drive", simplify = True)
dk = ox.geometries_from_bbox(bbox_fig[0],bbox_fig[1],bbox_fig[2],bbox_fig[3],tags={"highway": True})

fig, ax = ox.plot_graph(G, node_size=0, bgcolor="w",edge_color="black", edge_linewidth=0.5,edge_alpha=0.5,figsize=(8, 12),show=False,close=False)

title_font = {'fontname':'Comic Sans MS'}   #'Comic Sans MS'
title_box = {'bbox':{'boxstyle':'round'},'bbox':{'fill':False}}


ax.set_title('Danmark',loc='center',y=1.1,**title_font,**title_box,size=25,alpha=0.8)
plt.suptitle(f'     $^\circ${point[0]}"N  $^\circ${point[1]}"E',y=1.13,**title_font)

plt.savefig('/Users/rasmusvahlgreen/Desktop/pic', format='png')


plt.show()
dk.shape


import osmnx as ox
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

def create_cmap():
    cmap = colors.LinearSegmentedColormap.from_list(name = "reds",colors=["black","grey"])

    return cmap


cmap = create_cmap()


img_folder = "images"
extension = "png"
size = 240

# Define city/cities
place = "Karlslunde"
point = (55.5733495, 12.2280125) #bredde/længdegrad = lattitude/longitude

bbox= (55.5855,55.5500,12.280,12.2140)
bbox_fig =(55.5855,55.5500,12.280,12.2140)
fp = f"./{img_folder}/{place}.{extension}"

gdf = ox.geometries_from_bbox(bbox[0],bbox[1],bbox[2],bbox[3],tags={"building": True})

fig, ax = ox.plot_footprints(gdf, alpha=0.7, show=False,close=False,color="black",bgcolor="white",dpi=100)
G = ox.graph_from_bbox(bbox[0],bbox[1],bbox[2],bbox[3], network_type="all", simplify = True)
edges = G.edges()
nodes_df,edges_df= ox.graph_to_gdfs(G)

## hver edge består af to noder
## hver node har længde bredde grader
#cmap for koordinaterne af noderne


#for edge, row in zip(edges, edges_df.iterrows()):
#   n1, n2 = edge
#    n_lat = max(nodes_df.loc[n1]["y"], nodes_df.loc[n2]["y"])
#    edges_df.update({id: f"{n1}/{n2}/{0}", "ll": n_lat})

#for edge in edges:
#    n1,n2= edge
#    n_lat = max(nodes_df.loc[n1]["y"], nodes_df.loc[n2]["y"])
#    print(n_lat)


#edge_color = ox.plot.get_edge_colors_by_attr(G,attr=,cmap = cmap)
ox.plot_graph(G,ax=ax, node_size=0, edge_color="black", edge_linewidth=1,edge_alpha=0.5,show=False,close=False,bbox=bbox_fig)


#street_names = []
#for _, edge in ox.graph_to_gdfs(G, nodes=False).fillna('').iterrows():
#    c = edge['geometry'].centroid
#    text = edge['name']
#    if text not in street_names:
#        street_names.append(text)
#        ax.annotate(text, (c.x, c.y), c='black', fontsize=8,family='calibri')


#######TITLE ############
#title_font = {'fontname':'Comic Sans MS'}   #'Comic Sans MS'
#title_box = {'bbox':{'boxstyle':'round'},'bbox':{'fill':False}}

#t44 = (55.573,12.228)

#ax.set_title('Karlslunde',loc='center',y=0.86,**title_font,**title_box,size=25,alpha=0.8)
#plt.suptitle(f'     $^\circ${t44[0]}"N  $^\circ${t44[1]}"E',y=0.84)
#ax.patch.set_edgecolor('black')

plt.show()


#Image(fp, height=size, width=size)



## hvid baggrund sorte bygninger og veje
## dpi mindst 300
## kant rundt om
## legend/titel
## ruter
## fade i kanterne


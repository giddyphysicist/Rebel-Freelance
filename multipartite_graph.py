# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 20:40:34 2023

@author: pgigg
"""

import itertools
import matplotlib.pyplot as plt
import networkx as nx

subset_sizes = [2,1,2,1,3,2,2]
subset_color = [
    "gold",
    "darkorange",
    "limegreen",
    "violet",
    "limegreen",
    "darkorange",
    "limegreen",
]


def multilayered_graph(*subset_sizes):
    extents = nx.utils.pairwise(itertools.accumulate((0,) + subset_sizes))
    layers = [range(start, end) for start, end in extents]
    G = nx.Graph()
    for (i, layer) in enumerate(layers):
        G.add_nodes_from(layer, layer=i)
    for layer1, layer2 in nx.utils.pairwise(layers):
        G.add_edges_from(itertools.product(layer1, layer2))
    return G


G = multilayered_graph(*subset_sizes)
color = [subset_color[data["layer"]] for v, data in G.nodes(data=True)]
pos = nx.multipartite_layout(G, subset_key="layer")
fig,ax = plt.subplots(figsize=(8, 8))
ax.set_facecolor('black')
nx.draw(G, pos)#, node_color=color, with_labels=False)
ax.axis("equal")
ax.set_facecolor('black')

plt.show()
import matplotlib

matplotlib.use("TkAgg")  # Ensure Tk backend

import matplotlib.pyplot as plt
import networkx as nx

plt.ion()  # Interactive mode
fig, ax = plt.subplots(figsize=(6, 6))
fig.canvas.manager.set_window_title("Logical Structure")


def visualize_graph(G):
    ax.clear()
    pos = nx.spring_layout(G, k=0.5, iterations=50)
    nx.draw(
        G,
        pos,
        ax=ax,
        with_labels=True,
        arrows=True,
        node_color="lightblue",
        edge_color="gray",
        node_size=2500,
        font_size=10,
    )
    ax.set_title("Logical Structure")
    fig.tight_layout()
    fig.canvas.draw()
    fig.canvas.flush_events()

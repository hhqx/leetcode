import networkx as nx
import matplotlib.pyplot as plt

class PlotGraph:

    def __init__(self):
        pass

    def show_Graph(self, G, node_labels=None, edge_labels=None):
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=False, node_size=1000, node_color='lightblue')
        if node_labels is not None:
            nx.draw_networkx_labels(G, pos, labels=node_labels)
        if edge_labels is not None:
            nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plt.show()

    def show_DiGraph(self, G, node_labels=None, edge_labels=None):
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=False, node_size=1000, node_color='lightblue', arrows=True)
        if node_labels is not None:
            nx.draw_networkx_labels(G, pos, labels=node_labels)
        if edge_labels is not None:
            nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plt.show()

    def show_MultiGraph(self, G, node_labels=None, edge_labels=None):
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=False, node_size=1000, node_color='lightblue', arrows=False)
        if node_labels is not None:
            nx.draw_networkx_labels(G, pos, labels=node_labels)
        if edge_labels is not None:
            nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plt.show()

    def show_MultiDiGraph(self, G, node_labels=None, edge_labels=None):
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=False, node_size=1000, node_color='lightblue', arrows=True)
        if node_labels is not None:
            nx.draw_networkx_labels(G, pos, labels=node_labels)
        if edge_labels is not None:
            nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plt.show()

    def plot(self, edges, graph_type=None, node_labels=None, edge_labels=None):
        def input_invaid():
            raise ValueError(
                "Invalid graph_type provided. Use one of the following: Graph, DiGraph, MultiGraph, MultiDiGraph.")
        if graph_type is None:
            if not all((
                    isinstance(edges[0], (tuple, list)) and len(edges[0]) == 2,
                    all(isinstance(edges[i], (tuple, list)) and len(edges[i]) == len(edges[i-1]) for i in range(len(edges)))
            )):
                input_invaid()

            if all(isinstance(edge, (tuple, list)) and len(edge) == 2 for edge in edges):
                G = nx.Graph(edges)
                self.show_Graph(G, node_labels, edge_labels)
            elif all(isinstance(edge, (tuple, list)) and len(edge) == 3 for edge in edges):
                G = nx.DiGraph(edges)
                self.show_DiGraph(G, node_labels, edge_labels)
            else:
                G = nx.MultiGraph(edges)
                self.show_MultiGraph(G, node_labels, edge_labels)
        elif graph_type == "Graph":
            G = nx.Graph(edges)
            self.show_Graph(G, node_labels, edge_labels)
        elif graph_type == "DiGraph":
            G = nx.DiGraph(edges)
            self.show_DiGraph(G, node_labels, edge_labels)
        elif graph_type == "MultiGraph":
            G = nx.MultiGraph(edges)
            self.show_MultiGraph(G, node_labels, edge_labels)
        elif graph_type == "MultiDiGraph":
            G = nx.MultiDiGraph(edges)
            self.show_MultiDiGraph(G, node_labels, edge_labels)
        else:
            input_invaid()

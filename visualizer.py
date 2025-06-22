import matplotlib.pyplot as plt
import networkx as nx

def draw_graph(graph, cycles=None):
    plt.clf()  # Clear previous graph

    pos = nx.spring_layout(graph)

    # Draw all nodes
    process_nodes = [n for n, attr in graph.nodes(data=True) if attr['type'] == 'process']
    resource_nodes = [n for n, attr in graph.nodes(data=True) if attr['type'] == 'resource']

    nx.draw_networkx_nodes(graph, pos, nodelist=process_nodes, node_color='lightblue', node_shape='o', label='Processes')
    nx.draw_networkx_nodes(graph, pos, nodelist=resource_nodes, node_color='lightgreen', node_shape='s', label='Resources')

    # Draw all edges
    request_edges = [(u, v) for u, v, d in graph.edges(data=True) if d['type'] == 'request']
    allocation_edges = [(u, v) for u, v, d in graph.edges(data=True) if d['type'] == 'allocation']

    nx.draw_networkx_edges(graph, pos, edgelist=request_edges, edge_color='blue', style='dashed', arrows=True)
    nx.draw_networkx_edges(graph, pos, edgelist=allocation_edges, edge_color='black', arrows=True)

    # Highlight Deadlock Cycle if found
    if cycles:
        for cycle in cycles:
            cycle_edges = list(zip(cycle, cycle[1:] + [cycle[0]]))
            nx.draw_networkx_edges(graph, pos, edgelist=cycle_edges, edge_color='red', width=2)

    nx.draw_networkx_labels(graph, pos)
    plt.title("Resource Allocation Graph")
    plt.axis('off')
    plt.legend()
    plt.show(block=False)
    plt.pause(0.1)

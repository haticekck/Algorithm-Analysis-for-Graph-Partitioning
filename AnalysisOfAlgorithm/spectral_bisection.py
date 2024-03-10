import time
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from scipy.sparse.linalg import eigsh


# Start - Random Graph with given entities ------
num_nodes = 10
edge_probability = 0.3


# generating a random graph
def generate_random_graph(nodes, probability):
    while True:
        graph = nx.erdos_renyi_graph(nodes, probability)
        if nx.is_connected(graph):
            return graph


# draw the graph   --not necessary
def plot_graph(graph):
    pos = nx.spring_layout(graph)  # Positioning nodes for a better visualization
    nx.draw(graph, pos, with_labels=True, font_weight='bold')
    plt.show()


random_graph = generate_random_graph(num_nodes, edge_probability)

while True:
    try:
        num_partitions = int(input("Enter the number of subsets: "))
        if num_partitions > 0:
            break
        else:
            print("Please enter a value greater than 0.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

start_time = time.time()


def spectral_partition(graph, k):
    laplacian_matrix = nx.laplacian_matrix(graph).astype(float)
    eigenvalues, eigenvectors = eigsh(laplacian_matrix, k, which='SM')  # SM: Smallest Magnitude
    partitions = np.argmax(eigenvectors, axis=1)
    return partitions


def plot_partitioned_graph(graph, partitions):
    pos = nx.spring_layout(graph)
    color_map = [f'C{p}' for p in partitions]
    nx.draw(graph, pos, with_labels=True, font_weight='bold', node_color=color_map)
    plt.show()


partition_result = spectral_partition(random_graph, num_partitions)
end_time = time.time()
execution_time = end_time - start_time
#print(f"\nExecution Time: {execution_time:.4f} seconds")
plot_partitioned_graph(random_graph, partition_result)


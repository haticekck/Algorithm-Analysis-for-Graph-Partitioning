import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
#from networkx import spectral_bisection
from scipy.linalg import eigvalsh

# Start - Random Graph with given entities ------
num_nodes = 5
edge_probability = 0.7

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
plot_graph(random_graph)

#bisection
def spectral_bisection(graph, k):
    laplacian_matrix = nx.laplacian_matrix(graph).toarray()

    # Retrieve only the eigenvalues, not eigenvectors
    eigenvalues = eigvalsh(laplacian_matrix)

    # Select the eigenvector corresponding to the second smallest eigenvalue
    second_smallest_eigenvector = eigenvalues[1]

    # Sort vertices based on values in the eigenvector
    sorted_vertices = np.argsort(second_smallest_eigenvector)

    # Divide the sorted vertices into k subsets
    subsets = np.array_split(sorted_vertices, k)

    return subsets


# End - Random Graph with given entities ------


# Start - Partitioning algorithm

# converting the graph to adjacent matrix

adjacency_matrix = nx.to_numpy_array(random_graph)
print(adjacency_matrix)


k = 3
result = spectral_bisection(random_graph, k)
print("Subsets:")
for i, subset in enumerate(result, 1):
    print(f"Subset {i}: {subset}")


# taking a value for k(number of partitions)
while True:
    try:
        num_partitions = int(input("Enter the number of subsets: "))
        if num_partitions > 0:
            break
        else:
            print("Please enter a value greater than 0.")
    except ValueError:
        print("Invalid input. Please enter an integer.")


# End - Partitioning algorithm  ----

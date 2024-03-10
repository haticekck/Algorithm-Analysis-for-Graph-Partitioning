import networkx as nx
import matplotlib.pyplot as plt
import random
import copy
import math
import time

num_nodes = 10
edge_probability = 0.3


def generate_random_graph(nodes, probability):
    while True:
        graph = nx.erdos_renyi_graph(nodes, probability)
        if nx.is_connected(graph):
            return graph


def initial_partition(graph, k):
    # Randomly assign nodes to partitions
    partitions = [random.randint(0, k - 1) for _ in range(graph.number_of_nodes())]
    return partitions


def cut_size(graph, partitions):
    cut = 0
    for edge in graph.edges():
        if partitions[edge[0]] != partitions[edge[1]]:
            cut += 1
    return cut


start_time = time.time()


def simulated_annealing(graph, k, temperature, cooling_rate, max_iterations):
    current_partitions = initial_partition(graph, k)
    best_partitions = copy.deepcopy(current_partitions)
    best_cut = cut_size(graph, best_partitions)

    for iteration in range(max_iterations):
        # Propose a move
        new_partitions = copy.deepcopy(current_partitions)
        node_to_move = random.choice(list(graph.nodes()))
        proposed_partition = random.randint(0, k - 1)
        new_partitions[node_to_move] = proposed_partition

        # Evaluate the new cut size
        new_cut = cut_size(graph, new_partitions)

        # Acceptance criteria: Only accept moves that reduce the cut size
        if new_cut < best_cut or random.random() < math.exp((best_cut - new_cut) / temperature):
            current_partitions = new_partitions
            best_cut = new_cut

        # Cooling schedule
        temperature *= 1 - cooling_rate

    return best_partitions


random_graph = generate_random_graph(num_nodes, edge_probability)

# Specify the number of partitions (k) and SA parameters
while True:
    try:
        k_partitions = int(input("Enter the number of subsets: "))
        if k_partitions > 0:
            break
        else:
            print("Please enter a value greater than 0.")
    except ValueError:
        print("Invalid input. Please enter an integer.")


initial_temperature = 1.0
cooling_rate = 0.02
max_iterations = 1000

# Apply Simulated Annealing for graph partitioning
result_partitions = simulated_annealing(random_graph, k_partitions, initial_temperature, cooling_rate, max_iterations)
end_time = time.time()
execution_time = end_time - start_time
print(f"\nExecution Time: {execution_time:.4f} seconds")


# Plot the graph with partitions
pos = nx.spring_layout(random_graph)
color_map = [f'C{p}' for p in result_partitions]
nx.draw(random_graph, pos, with_labels=True, font_weight='bold', node_color=color_map)
plt.show()

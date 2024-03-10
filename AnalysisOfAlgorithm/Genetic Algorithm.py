import networkx as nx
import random
import matplotlib.pyplot as plt
import time


def generate_random_connected_graph(nodes, probability):
    while True:
        graph = nx.erdos_renyi_graph(nodes, probability)
        if nx.is_connected(graph):
            return graph


def draw_partitioned_graph(graph, partition):
    pos = nx.spring_layout(graph)
    color_map = []
    for i, part in enumerate(partition):
        color_map.extend([i] * len(part))
    cmap = plt.cm.get_cmap('viridis', num_partitions)
    nx.draw(graph, pos, with_labels=True, font_weight='bold', node_color=color_map, cmap=cmap)
    plt.show()


def cut_size(graph, partition):
    cut_size = 0
    for i in range(len(partition)):
        for j in range(i + 1, len(partition)):
            cut_size += cut(graph, partition[i], partition[j])
    return cut_size


def cut(graph, partition_a, partition_b):
    cut_size = 0
    for node_a in partition_a:
        for node_b in partition_b:
            if graph.has_edge(node_a, node_b):
                cut_size += 1
    return cut_size


start_time = time.time()


def genetic_algorithm(graph, num_partitions, generations=100, population_size=20, mutation_rate=0.1):
    nodes = list(graph.nodes)
    population = initialize_population(nodes, population_size, num_partitions)
    for generation in range(generations):
        population = next_generation(graph, population, mutation_rate)
    best_partition = max(population, key=lambda p: -fitness(graph, p))
    return best_partition


def initialize_population(nodes, population_size, num_partitions):
    return [random_partition(nodes, num_partitions) for _ in range(population_size)]


def random_partition(nodes, num_partitions):
    random.shuffle(nodes)
    return [nodes[i::num_partitions] for i in range(num_partitions)]


def fitness(graph, partition):
    return -cut_size(graph, partition)  # Negative cut size to maximize fitness


def crossover(parent1, parent2):
    crossover_point = random.randint(1, min(len(parent1), len(parent2)) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2


def mutate(partition, mutation_rate):
    if random.random() < mutation_rate:
        mutation_point = random.randint(0, len(partition) - 1)
        partition[mutation_point].append(partition[mutation_point].pop(0))
    return partition


def next_generation(graph, population, mutation_rate):
    fitness_scores = [(partition, fitness(graph, partition)) for partition in population]
    sorted_population = [p for p, _ in sorted(fitness_scores, key=lambda x: x[1], reverse=True)]
    new_population = sorted_population[:len(sorted_population) // 2]  # Keep the top half
    while len(new_population) < len(population):
        parent1, parent2 = random.choices(sorted_population, k=2)
        child1, child2 = crossover(parent1, parent2)
        child1 = mutate(child1, mutation_rate)
        child2 = mutate(child2, mutation_rate)
        new_population.extend([child1, child2])
    return new_population


# User input for the number of partitions
while True:
    try:
        num_partitions = int(input("Enter the number of subsets (k): "))
        if num_partitions > 0:
            break
        else:
            print("Please enter a value greater than 0.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

num_nodes = 100
edge_probability = 0.3
random_graph = generate_random_connected_graph(num_nodes, edge_probability)

result_partition = genetic_algorithm(random_graph, num_partitions)
end_time = time.time()
execution_time = end_time - start_time
print(f"\nExecution Time: {execution_time:.4f} seconds")
"""draw_partitioned_graph(random_graph, result_partition)"""

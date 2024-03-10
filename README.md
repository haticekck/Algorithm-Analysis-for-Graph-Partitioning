# Graph Partition Optimization

This project explores various algorithms for solving the Graph Partitioning Problem, aiming to divide the vertices of a graph into a specified number of subsets while minimizing the number of edges that cross between subsets. The implemented algorithms include Spectral Bisection, Simulated Annealing, and Genetic Algorithms.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Algorithms](#algorithms)
- [Usage](#usage)
- [Known Limitations](#known_limitations)

## Introduction

The Graph Partitioning Problem involves partitioning the vertices of a graph into a specified number of subsets such that the number of edges crossing between subsets is minimized. This problem arises in various domains, including network optimization, VLSI design, and parallel computing.

## Features

- Implements Spectral Bisection, Simulated Annealing, and Genetic Algorithms for graph partitioning.
- Allows users to specify the number of partitions.
- Provides visualization capabilities to visualize the partitioned graph.
- Supports custom graph input or randomly generated graphs.

## Algorithms

### Spectral Bisection

The Spectral Bisection algorithm partitions the graph by recursively bisecting it into two parts based on the eigenvector corresponding to the second smallest eigenvalue of the Laplacian matrix.

### Simulated Annealing

Simulated Annealing is a stochastic optimization technique that iteratively explores the solution space, accepting probabilistically worse solutions to escape local optima.

### Genetic Algorithms

Genetic Algorithms are evolutionary algorithms inspired by biological evolution. They maintain a population of candidate solutions, iteratively applying selection, crossover, and mutation operators to evolve towards optimal solutions.

## Usage

To use the project, follow these steps:

1. Choose the desired algorithm and specify parameters such as the number of partitions.
2. Provide the input graph, either as a custom graph or a randomly generated one.
3. Run the selected algorithm to obtain the partitioned graph.
4. Visualize the partitioned graph to analyze the results.

## Known Limitations

- **Graph Size:** The performance of the algorithms may degrade for very large graphs due to increased computation time and memory requirements.
  
- **Algorithm Complexity:** Some algorithms may have exponential time complexity, making them less suitable for graphs with a large number of vertices or partitions.

- **Optimality:** The solutions obtained by the implemented algorithms may not always be optimal due to the heuristic nature of the approaches.

- **Parameter Sensitivity:** The performance of certain algorithms, such as Simulated Annealing and Genetic Algorithms, may be sensitive to the choice of parameters such as temperature schedule or mutation rate.

- **Graph Structure:** The effectiveness of the algorithms may vary depending on the structure of the input graph, with some algorithms performing better on certain types of graphs than others.

- **Dependency on Initial Configuration:** The quality of the partitioning obtained by some algorithms may depend on the initial configuration or random seed, leading to potential variations in results for different runs.

- **Convergence Speed:** Convergence to the optimal solution may be slow for large or complex graphs, requiring longer execution times or additional iterations.

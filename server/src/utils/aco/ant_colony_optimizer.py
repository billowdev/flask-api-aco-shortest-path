import numpy as np

class AntColonyOptimizer:
    def __init__(self, num_ants, evaporation_rate, alpha, beta, q, graph):
        self.num_ants = num_ants
        self.evaporation_rate = evaporation_rate
        self.alpha = alpha
        self.beta = beta
        self.q = q
        self.graph = graph
        self.pheromone = np.ones_like(graph['distances']) / len(graph['distances'])

    def run(self, start_node, iterations):
        num_locations = len(self.graph['distances'])
        best_distance = float('inf')
        best_path = None

        for i in range(iterations):
            # Run one iteration of the ACO algorithm
            paths = []
            distances = []

            for j in range(self.num_ants):
                path, distance = self._find_path(start_node)
                paths.append(path)
                distances.append(distance)

                if distance < best_distance:
                    best_distance = distance
                    best_path = path

            # Update the pheromone trails
            self._update_pheromone_trails(paths, distances)

        return best_path, best_distance

    def _find_path(self, start_node):
        num_locations = len(self.graph['distances'])
        visited = np.zeros(num_locations, dtype=bool)
        visited[start_node] = True
        path = [start_node]
        distance = 0

        while len(path) < num_locations:
            # Choose the next node
            node = self._choose_next_node(path[-1], visited)

            # Update the visited nodes and the path
            visited[node] = True
            path.append(node)
            distance += self.graph['distances'][path[-2], path[-1]]

        # Add the distance back to the start node to complete the path
        distance += self.graph['distances'][path[-1], start_node]

        return path, distance

    def _choose_next_node(self, current_node, visited):
        num_locations = len(self.graph['distances'])
        unvisited = np.logical_not(visited)
        pheromone = self.pheromone[current_node, unvisited]
        distances = self.graph['distances'][current_node, unvisited]
        attractiveness = (1.0 / distances)**self.beta * (pheromone)**self.alpha
        probability = attractiveness / np.sum(attractiveness)
        next_node = np.random.choice(np.arange(num_locations)[unvisited], p=probability)

        return next_node

    def _update_pheromone_trails(self, paths, distances):
        num_locations = len(self.graph['distances'])
        pheromone_delta = np.zeros_like(self.pheromone)

        for i in range(len(paths)):
            for j in range(len(paths[i]) - 1):
                node1 = paths[i][j]
                node2 = paths[i][j+1]
                pheromone_delta[node1, node2] += self.q / distances[i]

        self.pheromone = (1 - self.evaporation_rate) * self.pheromone + pheromone_delta

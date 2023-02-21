import random

# Define the location data
locations = [
    { 
        "name":"A",
        "lat": 17.194128075459155,
        "lng" : 104.09076405880325
    },
    {
        "name":"B",
        "lat": 17.191457535779367,
        "lng" :  104.08921388934444
    },
]

# Define the distance matrix
distances = []
for i in range(len(locations)):
    row = []
    for j in range(len(locations)):
        lat1, lng1 = locations[i]["lat"], locations[i]["lng"]
        lat2, lng2 = locations[j]["lat"], locations[j]["lng"]
        distance = ((lat1-lat2)**2 + (lng1-lng2)**2)**0.5 * 111.12
        row.append(distance)
    distances.append(row)

# Initialize the pheromone matrix with an initial value
pheromone_initial = 0.1
pheromones = [[pheromone_initial for j in range(len(locations))] for i in range(len(locations))]

# Set the parameters for the ACO algorithm
num_ants = 10
alpha = 1
beta = 2
evaporation_rate = 0.1
q = 1
num_iterations = 50

# Run the ACO algorithm
shortest_path = None
shortest_distance = float("inf")
for iteration in range(num_iterations):
    for ant in range(num_ants):
        # Initialize the ant's path
        path = [random.randint(0, len(locations)-1)]
        visited = set(path)

        # Build the ant's path
        while len(visited) < len(locations):
            # Choose the next location based on the pheromone and distance values
            current_location = path[-1]
            p = [0] * len(locations)
            for j in range(len(locations)):
                if j not in visited:
                    p[j] = pheromones[current_location][j]**alpha * (1/distances[current_location][j])**beta
            next_location = random.choices(range(len(locations)), weights=p)[0]

            # Add the next location to the ant's path
            path.append(next_location)
            visited.add(next_location)

        # Update the pheromone matrix based on the ant's path
        distance = sum(distances[path[i]][path[i+1]] for i in range(len(path)-1))
        if distance < shortest_distance:
            shortest_path = path
            shortest_distance = distance
        for i in range(len(path)-1):
            pheromones[path[i]][path[i+1]] = (1-evaporation_rate)*pheromones[path[i]][path[i+1]] + q/distance

    # Evaporate the pheromone matrix
    for i in range(len(locations)):
        for j in range(len(locations)):
            pheromones[i][j] *= (1-evaporation_rate)

# Print the shortest path and distance in kilometers
print("Shortest path:", [locations[i]["name"] for i in shortest_path])
print("Shortest distance:", shortest_distance, "km")

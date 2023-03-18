from src.utils.aco.ant_colony_optimizer import AntColonyOptimizer
import numpy as np

# Define a function to calculate the distance between two locations
def distance(loc1, loc2):
	lat1, lng1 = loc1
	lat2, lng2 = loc2
	return np.sqrt((lat1 - lat2)**2 + (lng1 - lng2)**2)



def aco_nearest_node_geo_location(locations, current_node):
	# Set up the ACO parameters
	num_ants = 10
	evaporation_rate = 0.1
	alpha = 1
	beta = 2
	q = 1
	iterations = 100
	# Create a distance matrix for the locations
	num_locations = len(locations)
	distances = np.zeros((num_locations, num_locations))
	for i in range(num_locations):
		for j in range(num_locations):
			distances[i][j] = distance((locations[i]["lat"], locations[i]["lng"]), (locations[j]["lat"], locations[j]["lng"]))

	# Create a graph for the ACO algorithm
	graph = {"distances": distances}

	# Find the index of the current node
	current_node_index = 0
	current_node_coords = (current_node[0], current_node[1])
	min_distance = float('inf')
	for i, location in enumerate(locations):
		location_coords = (location["lat"], location["lng"])
		d = distance(current_node_coords, location_coords)
		if d < min_distance:
			min_distance = d
			current_node_index = i

	# Set up the ACO optimizer
	aco = AntColonyOptimizer(num_ants=num_ants,
							 evaporation_rate=evaporation_rate,
							 alpha=alpha,
							 beta=beta,
							 q=q,
							 graph=graph)

	# Run the ACO algorithm
	best_path, best_distance = aco.run(start_node=current_node_index, iterations=iterations)

	# Find the index of the nearest location
	nearest_location_index = best_path[1]

	# Return the nearest location
	return locations[nearest_location_index]['bid']


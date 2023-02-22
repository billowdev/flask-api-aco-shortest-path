from src.utils.aco.ant_colony_optimizer import AntColonyOptimizer
import numpy as np

my_locations = [
	{
		"bid": "A7",
		"name": "A7",
				"desc": "ตึก 7",
				"lat": 17.191058760990806,
				"lng": 104.0894708420397,
	},
	{
		"bid": "A9",
		"name": "A9",
		"desc": "ตึก 9",
		"lat": 17.190634027635916,
				"lng": 104.09040683236034
	},
	{
		"bid": "A6",
		"name": "A6",
		"desc": "ตึก 6",
				"lat": 17.190970159860075,
				"lng":  104.08848902422882
	},
	{
		"bid": "C4",
		"name": "C4",
		"desc": "แยกเนเซี่ยม",
				"lat": 17.189400286942945,
				"lng":  104.09174171837972
	},
	{
		"bid": "C5",
		"name": "C5",
		"desc": "ทางสามแยกทางเข้าครุศาสตร์",
				"lat": 17.188738469975437,
				"lng":  104.09137406371342
	},
	{
		"bid": "C1",
		"name": "C1",
		"desc": "หน้าอาคาร 1 ทางเข้าอาคารครุศาสตร์",
				"lat": 17.189578289590823,
				"lng":  104.09041195449454
	}

]

# Define a function to calculate the distance between two locations
def distance(loc1, loc2):
	return np.sqrt((loc1['lat'] - loc2['lat'])**2 + (loc1['lng'] - loc2['lng'])**2)

# Define the ACO algorithm
def aco_nearest_node(locations, current_node):
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
			distances[i][j] = distance(locations[i], locations[j])

	# Create a graph for the ACO algorithm
	graph = {"distances": distances}

	# Find the index of the current node
	current_node_index = [i for i, loc in enumerate(locations) if loc['bid'] == current_node][0]
	print(current_node_index)
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
	# print(best_path[1])
	# print(locations[nearest_location_index])
	# Return the nearest location
	return locations[nearest_location_index]['bid']


a = aco_nearest_node(my_locations, "C1")
print(a)
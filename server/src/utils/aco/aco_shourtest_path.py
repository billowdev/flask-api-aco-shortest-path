import random
import sys
# Define the location data
locations = [
	{
		"name": "A7",
				"desc": "ตึก 7",
				"lat": 17.191058760990806,
				"lng": 104.0894708420397,
	},
	{
		"name": "A9",
		"desc": "ตึก 9",
		"lat": 17.190634027635916,
				"lng": 104.09040683236034
	},
	{
		"name": "A6",
		"desc": "ตึก 6",
				"lat": 17.190970159860075,
				"lng":  104.08848902422882
	},
	{
		"name": "C4",
		"desc": "แยกเนเซี่ยม",
				"lat": 17.189400286942945,
				"lng":  104.09174171837972
	},
	{
		"name": "C5",
		"desc": "ทางสามแยกทางเข้าครุศาสตร์",
				"lat": 17.188738469975437,
				"lng":  104.09137406371342
	},
	{
		"name": "C1",
		"desc": "หน้าอาคาร 1 ทางเข้าอาคารครุศาสตร์",
				"lat": 17.189578289590823,
				"lng":  104.09041195449454
	}

]


def shortest_path(locations, req_start, req_goal):
	"""shortest_path is function that using ant colony algorithm for find shortest path 
	from start and goal

	Args:
		locations (_type_): location that mean building models
		req_start (_type_): start location
		req_goal (_type_): goal location
	"""
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
	pheromones = [[pheromone_initial for j in range(
		len(locations))] for i in range(len(locations))]

	# Set the parameters for the ACO algorithm
	num_ants = 10
	alpha = 1
	beta = 2
	evaporation_rate = 0.1
	q = 1
	num_iterations = 50

	# Define the start and goal states
	start_state = locations.index(
		next(location for location in locations if location["name"] == req_start))
	goal_state = locations.index(
		next(location for location in locations if location["name"] == req_goal))

	# Run the ACO algorithm
	shortest_path = None
	shortest_distance = float("inf")
	for iteration in range(num_iterations):
		for ant in range(num_ants):
			# Initialize the ant's path
			path = [start_state]
			visited = set(path)

			# Build the ant's path
			while len(visited) < len(locations):
				# Choose the next location based on the pheromone and distance values
				current_location = path[-1]
				p = [0] * len(locations)
				for j in range(len(locations)):
					if j not in visited:
						p[j] = pheromones[current_location][j]**alpha * \
							(1/distances[current_location][j])**beta
				next_location = random.choices(
					range(len(locations)), weights=p)[0]

				# Add the next location to the ant's path
				path.append(next_location)
				visited.add(next_location)

			# Update the pheromone matrix based on the ant's path
			distance = sum(distances[path[i]][path[i+1]]
						   for i in range(len(path)-1))
			if distance < shortest_distance and goal_state in path:
				shortest_path = path
				shortest_distance = distance
			for i in range(len(path)-1):
				pheromones[path[i]][path[i+1]
									] = (1-evaporation_rate)*pheromones[path[i]][path[i+1]] + q/distance
		# Evaporate the pheromone matrix
		for i in range(len(locations)):
			for j in range(len(locations)):
				pheromones[i][j] *= (1-evaporation_rate)

	# Print the shortest path and distance in kilometers
	start_name = locations[start_state]["name"]
	goal_name = locations[goal_state]["name"]
	shortest_path_names = [locations[i]["name"] for i in shortest_path]
	# shortest_path_desc = [locations[i]["desc"].encode('utf-8') for i in shortest_path]


	# my_desc = locations[0]['desc']
	# sys.stdout.buffer.write(my_desc.encode('utf-8'))
	# print(f"Shortest path from {start_name} to {goal_name}: {shortest_path_desc}")
	# print(f"Shortest path from {start_name} to {goal_name}: {shortest_path_names}")
	# print(f"Shortest distance: {shortest_distance:.2f} km")
	return [shortest_path_names, shortest_distance]
	




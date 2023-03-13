from decimal import Decimal
import random
import sys
# Define the location data


def aco_shortest_path(locations, req_start, req_goal):
    """shortest_path is function that using ant colony algorithm for find shortest path 
    from start and goal

    Args:
            locations (_type_): location that mean building models
            req_start (_type_): start location
            req_goal (_type_): goal location
    """
    """การทำงานของฟังก์ชัน
    ฟังก์ชันนี้ต้องการ อากิวเมนต์ locations, req_start, และ req_goal
    เป็นฟังก์ชันในการใช้ แอนต์โคโรนี อัลกอริทึมในการหา เส้นทางที่สั้นที่สุด

    """
    # Define the distance matrix
    """
        กำหนดตัวแปร distances เพื่อเก็บระยะทางระหว่างสถานที่แต่ละคู่
        
        การ loop สองชั้นดังโค้ดด้านล่างเป็นการ วนซ้ำทุกตำแหน่งแล้วคำนวณหาระยะห่างระหว่างสถานที่
    """
    distances = []
    for i in range(len(locations)):
        row = []
        for j in range(len(locations)):
            lat1, lng1 = locations[i]["lat"], locations[i]["lng"]
            lat2, lng2 = locations[j]["lat"], locations[j]["lng"]

            lat1, lng1 = float(lat1), float(lng1)
            lat2, lng2 = float(lat2), float(lng2)

            # print(lat1, lng2)
            # print(f"deubg : {type(104.09137406371342)}")
            # print(f"deubg : {type(lat1)}")
            # print(f"deubg : {lat1}")
            # print(f"deubg : {type(float(lat1))}")
            # print(f"deubg : {float(lat1)}")

            distance = ((lat1-lat2)**2 + (lng1-lng2)**2)**0.5 * 111.12
            # distance = ((lat1-lat2)**Decimal(2) + (lng1-lng2)**2)**Decimal(0.5) * Decimal(111.12)
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
        next(location for location in locations if location["bid"] == req_start))

    goal_state = locations.index(
        next(location for location in locations if location["bid"] == req_goal))

    # Run the ACO algorithm
    shortest_path = None
    shortest_distance = float("inf")
    for iteration in range(num_iterations):
        for ant in range(num_ants):
            # Initialize the ant's path
            path = [start_state]
            visited = set(path)
            # print(f"debug: {visited}"")

            # Build the ant's path
            while len(visited) < len(locations):
                # Choose the next location based on the pheromone and distance values
                current_location = path[-1]
                p = [0] * len(locations)
                for j in range(len(locations)):
                    if j not in visited:
                        p[j] = pheromones[current_location][j]**alpha * \
                            (1/distances[current_location][j])**beta
                        # p[j] = Decimal(pheromones[current_location][j])**Decimal(alpha) * \
                        # Decimal((1/distances[current_location][j])) **Decimal(beta)
                # print("========== debug: can run ==========")
                next_location = random.choices(
                    range(len(locations)), weights=p)[0]

                # Add the next location to the ant's path
                path.append(next_location)
                visited.add(next_location)

            # Update the pheromone matrix based on the ant's path
            # print("==========debug : can run ==========")
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
    start_bid = locations[start_state]["bid"]
    goal_bid = locations[goal_state]["bid"]
    shortest_path_names = [locations[i]["bid"] for i in shortest_path]
    # shortest_path_desc = [locations[i]["desc"].encode('utf-8') for i in shortest_path]

    # my_desc = locations[0]['desc']
    # sys.stdout.buffer.write(my_desc.encode('utf-8'))
    # print(f"Shortest path from {start_name} to {goal_name}: {shortest_path_desc}")
    # print(f"Shortest path from {start_name} to {goal_name}: {shortest_path_names}")
    # print(f"Shortest distance: {shortest_distance:.2f} km")
    # return [shortest_path_names, shortest_distance, start_bid, goal_bid]
    return {
        "best_path": shortest_path_names, 
        "distance":shortest_distance,
        "start":start_bid, 
        "goal":goal_bid
    }

from ant_colony_algorithm.Ant_Colony import AntColony


class AntColonyAlgorithm:

    def __init__(self, usa_map, ant_colony_size, iterations_nr, alfa, beta, evaporation_speed, min_pheromones_amount):
        self.usa_map = usa_map
        self.ant_colony_size = ant_colony_size
        self.iterations_nr = iterations_nr
        self.alfa = alfa
        self.beta = beta
        self.evaporation_speed = evaporation_speed
        self.min_pheromones_amount = min_pheromones_amount

        self.ant_colony = AntColony(ant_colony_size)  # create ant colony
        usa_map.add_pheromones(min_pheromones_amount)  # init minimum pheromones amount on the links

    def start(self, source_city, destination_city):
        best_path = []

        for iteration in range(self.iterations_nr):
            i = 0
            for ant in self.ant_colony.ants:
                pass
                # ant is looking for path from source to destination
                # comparison of current path with the best_path

            for ant in self.ant_colony.ants:
                pass
                # actualization of pheromones on current path found by ant
                # truncate current path

            self.usa_map.evaporate_pheromones(self.evaporation_speed, self.min_pheromones_amount)

        return best_path

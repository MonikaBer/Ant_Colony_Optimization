from ant_colony_algorithm.AntColony import AntColony
from ant_colony_algorithm.Link import Link


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
        usa_map.init_pheromones(min_pheromones_amount)  # init minimum pheromones amount on the links

    def start(self, source_city, destination_city):
        best_path = []
        best_path_cost = 0.0

        for iteration in range(self.iterations_nr):
            for ant in self.ant_colony.ants:
                ant.path = self.find_path(source_city, destination_city)  # ant is looking for path from source to destination
                ant.count_total_path_cost()
                if best_path == [] or ant.total_path_cost < best_path_cost:
                    best_path = ant.path
                    best_path_cost = ant.total_path_cost

            for ant in self.ant_colony.ants:
                self.usa_map.add_pheromones(ant.path, ant.total_path_cost)  # actualization of pheromones on current path (found by ant)

            self.usa_map.evaporate_pheromones(self.evaporation_speed, self.min_pheromones_amount)

        return best_path, best_path_cost

    def find_path(self, source_city, destination_city):
        visited_nodes = []
        path = []
        city = source_city
        # while city != destination_city:
        #     pass
        return path

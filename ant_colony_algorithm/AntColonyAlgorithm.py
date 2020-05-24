from ant_colony_algorithm.AntColony import AntColony
import random

from ant_colony_algorithm.Node import Node


class AntColonyAlgorithm:

    def __init__(self, usa_map, ant_colony_size, iterations_nr, alpha, beta, evaporation_speed, min_pheromones_amount):
        self.usa_map = usa_map
        self.ant_colony_size = ant_colony_size
        self.iterations_nr = iterations_nr
        self.alpha = alpha
        self.beta = beta
        self.evaporation_speed = evaporation_speed
        self.min_pheromones_amount = min_pheromones_amount

        self.ant_colony = AntColony(ant_colony_size)  # create ant colony
        usa_map.init_pheromones(min_pheromones_amount)  # init minimum pheromones amount on the links

    def start(self, source_city, target_city):
        best_path = []
        best_path_cost = 0.0

        for iteration in range(self.iterations_nr):
            for ant in self.ant_colony.ants:
                ant.path = self.find_path(self.usa_map.get_node(source_city), self.usa_map.get_node(target_city))  # ant is looking for path from source to destination
                ant.count_total_path_cost()
                if best_path == [] or ant.total_path_cost < best_path_cost:
                    best_path = ant.path
                    best_path_cost = ant.total_path_cost

            for ant in self.ant_colony.ants:
                self.usa_map.add_pheromones(ant.path,
                                            ant.total_path_cost)  # actualization of pheromones on current path (found by ant)

            self.usa_map.evaporate_pheromones(self.evaporation_speed, self.min_pheromones_amount)

        return best_path, best_path_cost

    def find_path(self, source_node, target_node):
        visited_nodes = []
        path = []
        probability_numerators = []
        probabilities = []
        current_node = source_node
        while current_node != target_node:
            #print(current_node.city)
            visited_nodes.append(current_node)
            probability_numerators.clear()
            probabilities.clear()
            for link in current_node.links:
                probability_numerators.append(self.count_probability_numerator(link.pheromones_amount, link.cost))
            probability = 0.0
            for numerator in probability_numerators:
                probability += numerator
            for numerator in probability_numerators:
                probabilities.append(numerator / probability)
            max_probability = -1.0
            links_numbers = []
            for nr, p in enumerate(probabilities):
                if p == -1.0 or p > max_probability:
                    max_probability = p
                    links_numbers.clear()
                    links_numbers.append(nr)
                if p == max_probability:
                    links_numbers.append(nr)

            selected_link_nr = links_numbers[random.randint(0, links_numbers.__len__()-1)]

            path.append(current_node.links[selected_link_nr])
            current_node = current_node.links[selected_link_nr].target_node
            print(current_node.city)

        return path

    def count_probability_numerator(self, pheromones_amount, cost):
        return pow(pheromones_amount, self.alpha) * pow(cost, self.beta)

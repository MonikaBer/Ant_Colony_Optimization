from ant_colony_algorithm.AntColony import AntColony
import random


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
                ant.path = self.find_path(self.usa_map.get_node(source_city), self.usa_map.get_node(
                    target_city))  # ant is looking for path from source to destination
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
            visited_nodes.append(current_node)
            probability_numerators.clear()
            probabilities.clear()
            links_numbers = []
            for nr, link in enumerate(current_node.links):
                if not AntColonyAlgorithm.is_node_in_visited_nodes(link.target_node, visited_nodes):
                    probability_numerators.append(self.count_probability_numerator(link.pheromones_amount, link.cost))
                    links_numbers.append(nr)
            probability = 0.0
            for numerator in probability_numerators:
                probability += numerator
            for numerator in probability_numerators:
                probabilities.append(numerator / probability)

            # probabilities, links_numbers = AntColonyAlgorithm.sort(probabilities, links_numbers)  # in decreasing order

            # random link
            rand = random.random()  # rand float from 0 to 1
            probability_sum = 0.0
            selected_link_nr = -1
            for nr, probability in enumerate(probabilities):
                probability_sum += probability
                if rand <= probability:
                    selected_link_nr = links_numbers[nr]
                    break

            if selected_link_nr == -1 or probability == 0:  # selected_link_nr is enaugh
                # TODO: lack of unvisited links from current node -> delete cycle from path; after third time do below instructions (restart ant route)
                current_node = source_node  # temporary solution
                visited_nodes.clear()  # temporary solution
                path.clear()  # temporary solution
                # print(current_node.city)
                continue
            else:
                path.append(current_node.links[selected_link_nr])
                current_node = current_node.links[selected_link_nr].target_node
                # print(current_node.city)

        return path

    def count_probability_numerator(self, pheromones_amount, cost):
        probability_numerator = pow(pheromones_amount, self.alpha) * pow(1 / pow(cost, 2), self.beta)
        return probability_numerator

    @staticmethod
    def sort(list_to_sort, related_list):
        for i in range(len(list_to_sort)):
            j = len(list_to_sort) - 1
            while j > i:
                if list_to_sort[j] > list_to_sort[j - 1]:
                    list_to_sort = AntColonyAlgorithm.exchange(list_to_sort, j, j - 1)
                    related_list = AntColonyAlgorithm.exchange(related_list, j, j - 1)
                j -= 1
        return list_to_sort, related_list

    @staticmethod
    def exchange(input_list, index1, index2):
        tmp = input_list[index1]
        input_list[index1] = input_list[index2]
        input_list[index2] = tmp
        return input_list

    @staticmethod
    def is_node_in_visited_nodes(checked_node, visited_nodes):
        if checked_node in visited_nodes:
            return True
        else:
            return False

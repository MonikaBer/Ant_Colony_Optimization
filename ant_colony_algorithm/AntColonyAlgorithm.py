from ant_colony_algorithm.Ant import Ant
from ant_colony_algorithm.AntColony import AntColony
import random

from ant_colony_algorithm.Navigator import Navigator
from graph.Path import Path


class AntColonyAlgorithm:

    def __init__(self, ant_colony_size, iterations_nr, alpha, beta, evaporation_speed, min_pheromones_amount):
        self.ant_colony_size = ant_colony_size
        self.iterations_nr = iterations_nr
        self.alpha = alpha
        self.beta = beta
        self.evaporation_speed = evaporation_speed
        self.min_pheromones_amount = min_pheromones_amount

    def start(self, source_city, target_city, usa_map):
        usa_map.init_pheromones(self.min_pheromones_amount)  # init minimum pheromones amount on the links
        best_path = Path([])

        ant_colony = AntColony(self.ant_colony_size, source_city)  # create ant colony

        for iteration in range(self.iterations_nr):
            for ant in ant_colony.ants:
                ant.path = self.find_path(usa_map.get_node(source_city), usa_map.get_node(target_city))  # ant is looking for path from source to destination
                if len(best_path) == 0 or ant.path < best_path:
                    best_path = ant.path
                    # self.usa_map.add_pheromones(ant.path)  # actualization of pheromones on current path (found by ant)   # triaaaaaaaal
                    print(str(best_path))
            for ant in ant_colony.ants:
                usa_map.add_pheromones(ant.path)  # actualization of pheromones on current path (found by ant)
            usa_map.evaporate_pheromones(self.evaporation_speed, self.min_pheromones_amount)
        return best_path

    def find_path(self, source_node, target_node):
        ant = Ant(source_node)
        current_node = source_node
        if source_node == target_node:
            return Path([], 0.0)
        while current_node != target_node:
            if current_node in ant.visited_nodes:
                is_ant_able_to_traverse = ant.handle_cycle(source_node)
                if not is_ant_able_to_traverse:
                    return Path([], 0.0)
            ant.visited_nodes.append(current_node)
            navigator = Navigator()
            for nr, link in enumerate(current_node.links):
                if len(ant.visited_nodes) > 1:
                    if link.target_node == ant.visited_nodes[-2]:
                        continue
                navigator.probability_numerators.append(self.count_probability_numerator(link.pheromones_amount, link.cost))
                navigator.links_numbers.append(nr)
            probability = 0.0
            for numerator in navigator.probability_numerators:
                probability += numerator
            for nr, numerator in enumerate(navigator.probability_numerators):
                navigator.probabilities.append(numerator / probability)

            rand = random.random()  # rand link (rand a number from 0.0 to 1.0)
            while rand == 0.0:
                rand = random.random()
            probability_sum = 0.0
            selected_link_nr = -1
            for nr, probability in enumerate(navigator.probabilities):
                probability_sum += probability
                if rand <= probability_sum:
                    selected_link_nr = navigator.links_numbers[nr]
                    break
            if selected_link_nr == -1:
                current_node = source_node
                ant.return_to_base()
                if ant.returns_to_base_number == 10:
                    return Path([], 0.0)
                continue
            the_next_link = [current_node.links[selected_link_nr]]
            the_next_link_cost = current_node.links[selected_link_nr].cost
            ant.path += (Path(the_next_link, the_next_link_cost))
            current_node = current_node.links[selected_link_nr].target_node
        return ant.path

    def count_probability_numerator(self, pheromones_amount, cost):
        # probability_numerator = pow(pheromones_amount, self.alpha) * pow(1 / pow(cost, 2), self.beta)
        probability_numerator = pow(pheromones_amount, self.alpha) * pow(1 / cost, self.beta)
        return probability_numerator

    @staticmethod
    def is_node_in_visited_nodes(checked_node, visited_nodes):
        if checked_node in visited_nodes:
            return True
        else:
            return False

    # @staticmethod
    # def sort(list_to_sort, related_list):
    #     for i in range(len(list_to_sort)):
    #         j = len(list_to_sort) - 1
    #         while j > i:
    #             if list_to_sort[j] > list_to_sort[j - 1]:
    #                 list_to_sort = AntColonyAlgorithm.exchange(list_to_sort, j, j - 1)
    #                 related_list = AntColonyAlgorithm.exchange(related_list, j, j - 1)
    #             j -= 1
    #     return list_to_sort, related_list

    # @staticmethod
    # def exchange(input_list, index1, index2):
    #     tmp = input_list[index1]
    #     input_list[index1] = input_list[index2]
    #     input_list[index2] = tmp
    #     return input_list

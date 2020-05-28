from ant_colony_algorithm.Ant import Ant
from ant_colony_algorithm.AntColony import AntColony

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
            navigator = Navigator(self.alpha, self.beta)
            navigator.count_probabilities(ant, current_node.links)

            next_link_nr = navigator.choose_next_link()
            if next_link_nr == -1:
                ant.return_to_base(source_node)
                if ant.returns_to_base_number == 10:
                    return Path([], 0.0)
                continue
            the_next_link = [current_node.links[next_link_nr]]
            the_next_link_cost = current_node.links[next_link_nr].cost
            ant.path += (Path(the_next_link, the_next_link_cost))
            current_node = current_node.links[next_link_nr].target_node
        return ant.path

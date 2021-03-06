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

    def start(self, source_city, target_city, usa_map, algo_type, taboo):
        usa_map.init_pheromones(self.min_pheromones_amount)  # init minimum pheromones amount on the links
        best_path = Path([])
        ant_colony = AntColony(self.ant_colony_size, source_city)  # create ant colony

        for iteration in range(self.iterations_nr):
            for ant in ant_colony.ants:
                ant.path = self.find_path(usa_map.get_node(source_city), usa_map.get_node(target_city), taboo)
                if algo_type == "CAS":
                    usa_map.add_pheromones(ant.path)
                if len(best_path) == 0 or ant.path < best_path:
                    best_path = ant.path
                    # print(str(best_path))
                    if algo_type == "MMAS":
                        usa_map.add_pheromones(ant.path)
            # for ant in ant_colony.ants:
            #     usa_map.add_pheromones(ant.path)
            usa_map.evaporate_pheromones(self.evaporation_speed, self.min_pheromones_amount)
        return best_path

    def find_path(self, source_node, target_node, taboo):
        if source_node == target_node:
            return Path([], 0.0)
        ant = Ant(source_node)
        ant.current_node = source_node
        while ant.current_node != target_node:
            if ant.current_node in ant.visited_nodes:
                is_ant_able_to_traverse = ant.handle_cycle(source_node)
                if not is_ant_able_to_traverse:
                    return Path([], 0.0)
            ant.visited_nodes.append(ant.current_node)
            navigator = Navigator(self.alpha, self.beta)
            navigator.count_probabilities(ant, taboo)

            next_link_nr = navigator.choose_next_link()
            if next_link_nr == -1:
                ant.return_to_base(source_node)
                if ant.returns_to_base_number == 10:
                    return Path([], 0.0)
                continue
            the_next_link = [ant.current_node.links[next_link_nr]]
            the_next_link_cost = ant.current_node.links[next_link_nr].cost
            ant.path += (Path(the_next_link, the_next_link_cost))
            ant.current_node = ant.current_node.links[next_link_nr].target_node
        return ant.path

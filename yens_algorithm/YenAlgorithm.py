from ant_colony_algorithm.AntColonyAlgorithm import AntColonyAlgorithm
from graph.Path import Path

from dijkstra.dijkstra import dijkstra


class YenAlgorithm:
    def __init__(self, ant_algo):
        self.ant_algo = ant_algo
        # self.best_paths = [Path(dijkstra(self.usa_map, start, stop))]
        # self.best_paths = [self.ant_algo.start(start, stop)]
        self.best_paths = []
        self.to_be_best_paths = set()

    def run(self, paths_to_find, usa_map, start, stop, algo_type):
        self.find_first_path(usa_map, start, stop, algo_type)
        if self.first_path_exists():
            for i in range(paths_to_find-1):
                usa_map.reset()
                for node_id in range(len(self.best_paths[-1])):
                    spur_city = self.get_spur_city(node_id)
                    root_path = self.get_root_path(node_id)
                    self.remove_links_to_best(usa_map, root_path, node_id)
                    self.complete_path(usa_map, root_path, spur_city, stop, algo_type)
                if not self.add_next_shortest():
                    break
        return self.best_paths

    def find_first_path(self, usa_map, start, stop, algo_type):
        self.best_paths.append(self.ant_algo.start(start, stop, usa_map, algo_type))

    def first_path_exists(self):
        if self.best_paths[0]:
            return True
        return False

    # def restore_map(self, usa_map):
    #     usa_map.reset()  # load full map
    #     # self.ant_algo.reset_pheromones()
    #     self.ant_algo.add_graph(self.usa_map)

    def add_next_shortest(self):
        if len(self.to_be_best_paths) == 0:
            return False
        next_shortest = min(self.to_be_best_paths)
        self.best_paths.append(next_shortest)
        self.to_be_best_paths.remove(next_shortest)
        return True

    def remove_links_to_best(self, usa_map, root_path, node_id):
        for path in self.best_paths:
            if root_path == Path(path[:node_id]):
                usa_map.remove_link(path[node_id])

    def complete_path(self, usa_map, root_path, spur_city, stop_city, algo_type):
        # shortest_complete = Path(dijkstra(self.usa_map, spur_city, self.stop))
        shortest_complete = self.ant_algo.start(spur_city, stop_city, usa_map, algo_type, [x.source_node.city for x in root_path])
        if shortest_complete:
            self.to_be_best_paths.add(root_path + shortest_complete)

    def get_root_path(self, node_id):
        return Path(self.best_paths[-1][:node_id])

    def get_spur_city(self, node_id):
        return self.best_paths[-1][node_id].source_node.city

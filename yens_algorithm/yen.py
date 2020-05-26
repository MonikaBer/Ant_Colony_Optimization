from ant_colony_algorithm.AntColonyAlgorithm import AntColonyAlgorithm
from graph.Path import Path

from dijkstra.dijkstra import dijkstra


class YenAlgorithm:
    def __init__(self, ant_algo, usa_map, start, stop):
        self.usa_map = usa_map
        self.start = start
        self.stop = stop
        self.ant_algo = ant_algo
        self.best_paths = [Path(dijkstra(self.usa_map, start, stop))]
        self.to_be_best_paths = set()

    def run(self, paths_to_find):
        if not self.first_path_exists():
            return
        for i in range(paths_to_find-1):
            self.restore_map()
            for node_id in range(len(self.best_paths[-1])):
                spur_city = self.get_spur_city(node_id)
                root_path = self.get_root_path(node_id)
                self.remove_links_to_best(root_path, node_id)
                self.complete_path(root_path, spur_city)
            if not self.add_next_shortest():
                break
        return self.best_paths

    def first_path_exists(self):
        if self.best_paths[0]:
            return True
        return False

    def restore_map(self):
        self.usa_map.reset()
        self.ant_algo.reset_pheromones()

    def add_next_shortest(self):
        if len(self.to_be_best_paths) == 0:
            return False
        next_shortest = min(self.to_be_best_paths)
        self.best_paths.append(next_shortest)
        self.to_be_best_paths.remove(next_shortest)
        return True

    def remove_links_to_best(self, root_path, node_id):
        for path in self.best_paths:
            if root_path == Path(path[:node_id]):
                self.usa_map.remove_link(path[node_id])

    def complete_path(self, root_path, spur_city):
        shortest_complete = Path(dijkstra(self.usa_map, spur_city, self.stop))
        if shortest_complete:
            self.to_be_best_paths.add(root_path + shortest_complete)

    def get_root_path(self, node_id):
        return Path(self.best_paths[-1][:node_id])

    def get_spur_city(self, node_id):
        return self.best_paths[-1][node_id].source_node.city

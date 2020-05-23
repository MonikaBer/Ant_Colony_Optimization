from ant_colony_algorithm.Link import Link


class Ant:

    def __init__(self):
        self.visitedNodes = []
        self.path = []
        self.total_path_cost = 0.0

    def find_path(self, source_city, destination_city):
        self.path.clear()
        self.path.append(Link(10, source_city, destination_city, 10.0, 50.0))

    def count_total_path_cost(self):
        self.total_path_cost = 0.0
        for link in self.path:
            self.total_path_cost += link.cost

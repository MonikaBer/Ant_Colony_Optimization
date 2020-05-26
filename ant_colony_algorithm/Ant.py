class Ant:

    def __init__(self):
        self.path = []
        self.total_path_cost = 0.0

    def count_total_path_cost(self):
        self.total_path_cost = 0.0
        for link in self.path:
            self.total_path_cost += link.cost

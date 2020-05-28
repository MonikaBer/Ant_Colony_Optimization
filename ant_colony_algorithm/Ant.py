from graph.Path import Path


class Ant:

    def __init__(self):
        self.path = Path([])
        self.cycles_number = 0
        self.returns_to_base_number = 0
        self.visited_nodes = []

    def return_to_base(self):
        self.visited_nodes.clear()
        self.path.clear()
        self.cycles_number = 0
        self.returns_to_base_number += 1

from graph.Path import Path


class Ant:

    def __init__(self, source_node):
        self.path = Path([])
        self.visited_nodes = []
        self.current_node = source_node
        self.cycles_number = 0
        self.returns_to_base_number = 0

    def return_to_base(self, source_node):
        self.path.clear()
        self.visited_nodes.clear()
        self.current_node = source_node
        self.cycles_number = 0
        self.returns_to_base_number += 1

    def handle_cycle(self, source_node):
        self.cycles_number += 1
        if self.cycles_number == 3:  # cycle occured for the third time -> move the ant to the source node
            self.return_to_base(source_node)
            if self.returns_to_base_number == 10:
                return False  # finish the ant's route
        else:  # only delete cycle from path
            self.path.delete_last_cycle()
            self.delete_last_cycle_from_visited_nodes()
        return True  # the last cycle is deleted or ant returned to the base

    def delete_last_cycle_from_visited_nodes(self):
        for i in range(len(self.visited_nodes)-2, -1, -1):
            if self.visited_nodes[i] == self.current_node:
                self.visited_nodes = self.visited_nodes[:i]
                break

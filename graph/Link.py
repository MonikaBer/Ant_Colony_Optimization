class Link:

    def __init__(self, id, source_node, target_node, capacity, cost):
        self.id = id
        self.source_node = source_node
        self.target_node = target_node
        self.capacity = capacity
        self.cost = cost
        self.pheromones_amount = 0.0

    def add_pheromones(self, pheromones_amount):
        self.pheromones_amount += pheromones_amount

    def evaporate_pheromones(self, evaporation_speed, min_pheromones_amount):
        self.pheromones_amount *= (1 - evaporation_speed)
        if self.pheromones_amount < min_pheromones_amount:
            self.pheromones_amount = min_pheromones_amount

    def __eq__(self, other):
        return self.id == other.id and self.source_node == other.source_node and self.target_node == other.target_node

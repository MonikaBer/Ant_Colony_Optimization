class Link:

    def __init__(self, link_id, source_city, target_city, capacity, cost):
        self.link_id = link_id
        self.source_city = source_city
        self.target_city = target_city
        self.capacity = capacity
        self.cost = cost
        self.pheromones_amount = 0.0

    def add_pheromones(self, pheromones_amount):
        self.pheromones_amount += pheromones_amount

    def evaporate_pheromones(self, evaporation_speed, min_pheromones_amount):
        self.pheromones_amount *= (1 - evaporation_speed)
        if self.pheromones_amount < min_pheromones_amount:
            self.pheromones_amount = min_pheromones_amount

class Link:

    def __init__(self, link_id, source_city, target_city, capacity, cost, pheromone_amount):
        self.link_id = link_id
        self.source_city = source_city
        self.target_city = target_city
        self.capacity = capacity
        self.cost = cost
        self.pheromone_amount = pheromone_amount

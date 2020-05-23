from ant_colony_algorithm.Ant import Ant


class AntColony:

    def __init__(self, colony_size):
        self.colony_size = colony_size
        self.ants = []
        for i in range(colony_size):
            self.ants.append(Ant())

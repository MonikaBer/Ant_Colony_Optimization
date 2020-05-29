import random


class Navigator:

    def __init__(self, alpha, beta):
        self.probability_numerators = []
        self.probabilities = []
        self. links_numbers = []
        self.alpha = alpha
        self.beta = beta

    def count_probabilities(self, ant, taboo):
        for nr, link in enumerate(ant.current_node.links):
            if link.target_node.city in taboo:
                continue
            if len(ant.visited_nodes) > 1:
                if link.target_node == ant.visited_nodes[-2]:
                    continue  # discard the last traversed link
            self.probability_numerators.append(self.count_probability_numerator(link.pheromones_amount, link.cost))
            self.links_numbers.append(nr)
        probability = 0.0
        for numerator in self.probability_numerators:
            probability += numerator
        for nr, numerator in enumerate(self.probability_numerators):
            self.probabilities.append(numerator / probability)

    def count_probability_numerator(self, pheromones_amount, cost):
        # probability_numerator = pow(pheromones_amount, self.alpha) * pow(1 / pow(cost, 2), self.beta)
        probability_numerator = pow(pheromones_amount, self.alpha) * pow(1 / cost, self.beta)
        return probability_numerator

    def choose_next_link(self):
        rand = random.random()  # rand link (rand a number from 0.0 to 1.0)
        while rand == 0.0:
            rand = random.random()
        probability_sum = 0.0
        for nr, probability in enumerate(self.probabilities):
            probability_sum += probability
            if rand <= probability_sum:
                selected_link_nr = self.links_numbers[nr]
                return selected_link_nr
        return -1

from graph.Link import Link
from graph.Node import Node


class USAMap:

    def __init__(self, input_file_name):
        self.nodes = []
        self.links = []
        self.removed_links = []

        input_file = open(input_file_name, "r")

        input_file.readline()
        for node in input_file:
            if node[:5] == "LINKS":
                break
            node = node.strip('\n')
            node_desc = node.split(' ')
            node_desc.pop()
            node_desc.pop(1)
            self.nodes.append(Node(node_desc[0], float(node_desc[1]), float(node_desc[2])))

        for link in input_file:
            link = link.strip('\n')
            link_desc = link.split(' ')
            link_desc.pop()
            link_desc.pop(1)
            for i in range(6):
                link_desc.pop(3)
            new_link = (Link(int(link_desc[0].lstrip('L')), self.get_node(link_desc[1]), self.get_node(link_desc[2]),
                             float(link_desc[3]),
                             float(link_desc[4])))
            self.links.append(new_link)
            for node in self.nodes:
                if node.city == link_desc[1]:
                    node.add_link(new_link)
                    break

        input_file.close()

    def init_pheromones(self, min_pheromones_amount):
        for link in self.links:
            # link.add_pheromones(min_pheromones_amount)
            link.pheromones_amount = min_pheromones_amount

    def add_pheromones(self, path, total_path_cost):
        for link in path:
            #self.links[link.id].pheromones_amount *= (1 + 1 / total_path_cost)
            self.links[link.id].pheromones_amount += 100         # try

    def evaporate_pheromones(self, evaporation_speed, min_pheromones_amount):
        for link in self.links:
            link.evaporate_pheromones(evaporation_speed, min_pheromones_amount)

    def get_node(self, city_name):
        for node in self.nodes:
            if node.city == city_name:
                return node

    def remove_link(self, link_to_remove):
        if link_to_remove in self.links:
            self.links.remove(link_to_remove)
            self.removed_links.append(link_to_remove)

    def reset(self):
        self.links += self.removed_links
        self.removed_links.clear()

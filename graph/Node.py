class Node:

    def __init__(self, city, x, y):
        self.city = city
        self.x = x
        self.y = y
        self.links = []  # links which go out from this node

    def add_link(self, link):
        self.links.append(link)

    def __eq__(self, other):
        return self.city == other.city

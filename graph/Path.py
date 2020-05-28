class Path:
    def __init__(self, links, cost=-1):
        self.links = links
        if cost == -1:
            self.cost = 0
            for link in links:
                self.cost += link.cost
        else:
            self.cost = cost

    def __eq__(self, other):
        return self.links == other.links

    def __str__(self):
        result = "path: "
        if len(self.links) > 0:
            for link in self.links:
                result += link.source_node.city + '-'
            result += self.links[-1].target_node.city
        return result

    def __hash__(self):
        return hash(str(self))

    def __lt__(self, other):
        return self.cost < other.cost

    def __getitem__(self, item):
        return self.links[item]

    def __len__(self):
        return len(self.links)

    def __add__(self, other):
        if not (len(self) == 0 or not len(other) == 0) and self.links[-1].target_node != other.links[0].source_node:
            raise ArithmeticError
        return Path(self.links + other.links, self.cost + other.cost)

    def __bool__(self):
        return bool(len(self.links))

    def clear(self):
        self.links = []
        self.cost = 0

    def len(self):
        return len(self.links)

    def delete_last_cycle(self):
        reference_node = self.links[-1].target_node
        for i in range(len(self.links) - 2, -1, -1):
            if self.links[i].source_node == reference_node:
                for j in range(i, len(self.links), 1):
                    self.cost -= self.links[j].cost
                self.links = self.links[:i]
                break

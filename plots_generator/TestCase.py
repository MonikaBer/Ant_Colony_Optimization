class TestCase:

    def __init__(self, param_value, costs, time):
        self.param_value = param_value
        self.costs = costs
        self.time = time

    def fill_costs(self, n):
        self.costs += [None] * (n-len(self.costs))

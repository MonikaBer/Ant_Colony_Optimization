import matplotlib.pyplot as plt

from plots_generator.TestCase import TestCase


class ParameterTester:

    def __init__(self, file_name):
        self.title = ""
        self.x_label = ""

        file = open(file_name, "r")
        file_name_after_split = file_name[13:].split("_")
        self.file_name = file_name
        algo_type = self.get_parameter_from_file_name(file_name_after_split)
        self.title += self.x_label + " " + algo_type + " plot"
        self.test_cases = []
        for line in file:
            line = line.strip('\n')
            line_after_split = line.split(",")
            self.test_cases.append(TestCase(line_after_split[0], line_after_split[1:len(line_after_split) - 1],
                                            line_after_split[len(line_after_split) - 1]))

    def draw_cost_plot(self):
        plt.clf()
        self.set_plot_parameters(True, "cost")
        x = []
        y = []
        for test_case in self.test_cases:
            for cost in test_case.costs:
                x.append(test_case.param_value)
                y.append(cost)
        plt.plot(x, y, 'go')
        plt.savefig("test_plots/" + self.file_name[13:] + "_cost_plot", dpi=72)

    def draw_time_plot(self):
        plt.clf()
        self.set_plot_parameters(True, "time")
        x = []
        y = []
        for test_case in self.test_cases:
            x.append(test_case.param_value)
            y.append(test_case.time)
        plt.plot(x, y, 'b*')
        plt.savefig("test_plots/" + self.file_name[13:] + "_time_plot", dpi=72)

    def set_plot_parameters(self, is_grid, y_label):
        plt.title(self.title)
        plt.grid(is_grid)
        plt.xlabel(self.x_label)
        plt.ylabel(y_label)

    def get_parameter_from_file_name(self, file_name_after_split):
        was_elem_test = False
        for elem in file_name_after_split:
            if elem == "test":
                self.x_label = self.x_label[:len(self.x_label) - 1]
                was_elem_test = True
                continue
            elif was_elem_test:
                return elem
            else:
                self.x_label += elem + " "

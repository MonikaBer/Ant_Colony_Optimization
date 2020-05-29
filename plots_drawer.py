import os

from plots_generator.ParameterTester import ParameterTester


def main():
    for item in os.listdir("test_outputs"):
        parameter_tester = ParameterTester("test_outputs/" + item)
        parameter_tester.draw_cost_plot()
        parameter_tester.draw_time_plot()


if __name__ == "__main__":
    main()

from ant_colony_algorithm.AntColonyAlgorithm import AntColonyAlgorithm
from ant_colony_algorithm.USAMap import USAMap


def main():
    usa_map = USAMap("input")
    ant_colony_algorithm = AntColonyAlgorithm(usa_map, ant_colony_size=40, iterations_nr=100, alfa=0.5, beta=0.5,
                                              evaporation_speed=0.7, min_pheromones_amount=1.0)

    best_path = ant_colony_algorithm.start("Los Angeles", "Atlanta")
    print(best_path)


if __name__ == "__main__":
    main()

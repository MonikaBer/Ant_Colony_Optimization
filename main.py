from ant_colony_algorithm.AntColonyAlgorithm import AntColonyAlgorithm
from ant_colony_algorithm.USAMap import USAMap


def main():
    usa_map = USAMap("input")
    ant_colony_algorithm = AntColonyAlgorithm(usa_map, ant_colony_size=40, iterations_nr=100, alfa=0.5, beta=0.5,
                                              evaporation_speed=0.7, min_pheromones_amount=1.0)

    best_path, best_path_cost = ant_colony_algorithm.start("Los Angeles", "Atlanta")
    print("The best path has the total cost: {}".format(best_path_cost))
    print("The best path:")
    for link in best_path:
        print("{} {} {}".format(link.source_city, link.target_city, link.cost))


if __name__ == "__main__":
    main()

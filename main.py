from ant_colony_algorithm.AntColonyAlgorithm import AntColonyAlgorithm
from ant_colony_algorithm.USAMap import USAMap


def main():
    usa_map = USAMap("input")
    ant_colony_algorithm = AntColonyAlgorithm(usa_map, ant_colony_size=30, iterations_nr=100, alpha=0.0, beta=5.0,
                                              evaporation_speed=0.5, min_pheromones_amount=0.5)

    best_path, best_path_cost = ant_colony_algorithm.start("LosAngeles", "Atlanta")
    print("The best path has the total cost: {}".format(best_path_cost))
    print("The best path:")
    for link in best_path:
        print("{} {} {}".format(link.source_node.city, link.target_node.city, link.cost))


if __name__ == "__main__":
    main()

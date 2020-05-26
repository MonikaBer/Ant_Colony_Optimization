from ant_colony_algorithm.AntColonyAlgorithm import AntColonyAlgorithm
from graph.USAMap import USAMap
from yens_algorithm.yen import YenAlgorithm
from dijkstra.dijkstra import dijkstra


def main():
    usa_map = USAMap("input_test")
    ant_colony_algorithm = AntColonyAlgorithm(usa_map, ant_colony_size=30, iterations_nr=100, alpha=0.0, beta=5.0,
                                              evaporation_speed=0.5, min_pheromones_amount=0.5)

    # best_path, best_path_cost = ant_colony_algorithm.start("C", "H")
    # print("The best path has the total cost: {}".format(best_path_cost))
    # print("The best path:")
    # for link in best_path:
    #     print("{} {} {}".format(link.source_node.city, link.target_node.city, link.cost))
    # print("path cost: ", best_path_cost)

    # yen = YenAlgorithm(ant_colony_algorithm, usa_map, "LosAngeles", "Atlanta")
    yen = YenAlgorithm(ant_colony_algorithm, usa_map, "C", "H")
    for n, path in enumerate(yen.run(10)):
        whole_cost = 0
        print(f"==============SCIEZKA {n}==============")
        for link in path.links:
            whole_cost += link.cost
            print("{} {} {}".format(link.source_node.city, link.target_node.city, link.cost))
        print("koszt calkowity: ", whole_cost)


if __name__ == "__main__":
    main()

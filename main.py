from ant_colony_algorithm.AntColonyAlgorithm import AntColonyAlgorithm
from graph.USAMap import USAMap
from yens_algorithm.YenAlgorithm import YenAlgorithm
from dijkstra.dijkstra import dijkstra


def main():
    usa_map = USAMap("input_test")
    ant_colony_algorithm = AntColonyAlgorithm(ant_colony_size=30, iterations_nr=100, alpha=1.0, beta=5.0,
                                              evaporation_speed=0.7, min_pheromones_amount=1.0)

    # best_path = ant_colony_algorithm.start("C", "H")
    # print("The best path has the total cost: {}".format(best_path.cost))
    # print("The best path:")
    # for link in best_path.links:
    #     print("{} {} {}".format(link.source_node.city, link.target_node.city, link.cost))
    #
    # print("\n\n")

    # best_path = ant_colony_algorithm.start("H", "C")
    # print("The best path has the total cost: {}".format(best_path.cost))
    # print("The best path:")
    # for link in best_path.links:
    #     print("{} {} {}".format(link.source_node.city, link.target_node.city, link.cost))

    # yen = YenAlgorithm(ant_colony_algorithm, usa_map, "LosAngeles", "Atlanta")
    yen = YenAlgorithm(ant_colony_algorithm)
    for n, path in enumerate(yen.run(20, usa_map, "C", "H", "CAS")):
        whole_cost = 0
        print(f"==============SCIEZKA {n}==============")
        for link in path.links:
            whole_cost += link.cost
            print("{} {} {}".format(link.source_node.city, link.target_node.city, link.cost))
        print("koszt calkowity: ", whole_cost)


if __name__ == "__main__":
    main()

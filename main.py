from ant_colony_algorithm.AntColonyAlgorithm import AntColonyAlgorithm
from graph.USAMap import USAMap
from yens_algorithm.YenAlgorithm import YenAlgorithm
import sys
from dijkstra.dijkstra import dijkstra


def main():
    if len(sys.argv) != 13 or sys.argv[1] == "help":
        print(
            "USAGE: python3 main.py input_file source target number_of_roots ant_colony_size ant_iterations alpha "
            "beta evaporation_speed min_pheromones ant_algo_type full_path")
        exit(1)
    input_file = sys.argv[1]
    start_city = sys.argv[2]
    stop_city = sys.argv[3]
    number_of_roots = int(sys.argv[4])
    ant_colony_size = int(sys.argv[5])
    ants_iterations = int(sys.argv[6])
    alpha = float(sys.argv[7].replace(',', '.'))
    beta = float(sys.argv[8].replace(',', '.'))
    evaporation_speed = float(sys.argv[9])
    min_pheromones = float(sys.argv[10])
    ant_algo_type = sys.argv[11]
    full_path = int(sys.argv[12])

    usa_map = USAMap(input_file)
    ant_colony_algorithm = AntColonyAlgorithm(ant_colony_size=ant_colony_size, iterations_nr=ants_iterations,
                                              alpha=alpha, beta=beta,
                                              evaporation_speed=evaporation_speed, min_pheromones_amount=min_pheromones)
    yen = YenAlgorithm(ant_colony_algorithm)

    if full_path:
        for n, path in enumerate(yen.run(number_of_roots, usa_map, start_city, stop_city, ant_algo_type)):
            print(n+1, path, path.cost)
    else:
        for n, path in enumerate(yen.run(number_of_roots, usa_map, start_city, stop_city, ant_algo_type)):
            print(path.cost, end=',')


if __name__ == "__main__":
    main()

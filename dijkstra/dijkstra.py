def dijkstra(usa_map, start, end):
    unvisited = set()
    for node in usa_map.nodes:
        unvisited.add(node.city)
    dist = dict()
    prev = dict()
    for node in unvisited:
        dist[node] = 9999999
        prev[node] = None
    dist[start] = 0

    while len(unvisited):
        min_dist = 9999999999
        for vertex in unvisited:
            if dist[vertex] < min_dist:
                u = vertex
                min_dist = dist[vertex]
        unvisited.remove(u)
        if u == end:
            break
        for link in usa_map.links:
            if link.source_node.city == u and link.target_node.city in unvisited:
                alt = dist[u] + link.cost
                if alt < dist[link.target_node.city]:
                    dist[link.target_node.city] = alt
                    prev[link.target_node.city] = u
    s = []
    if prev[u] is not None or u == start:
        while u is not None:
            s.append(u)
            u = prev[u]
    s.reverse()
    result = []

    for n, city in enumerate(s[:-1]):
        for link in usa_map.links:
            if link.source_node.city == city and link.target_node.city == s[n+1]:
                result.append(link)
                break
    return result

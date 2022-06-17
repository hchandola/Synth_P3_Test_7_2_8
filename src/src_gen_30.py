from typing import List

def sat308(path: List[int], weights=[{1: 20, 2: 1}, {2: 2, 3: 5}, {1: 10}], bound=11):
    return path[0] == 0 and path[-1] == 1 and sum(weights[a][b] for a, b in zip(path, path[1:])) <= bound
def sol308(weights=[{1: 20, 2: 1}, {2: 2, 3: 5}, {1: 10}], bound=11):
    """
    Find a path from node 0 to node 1, of length at most bound, in the given digraph.
    weights[a][b] is weight on edge [a,b] for (int) nodes a, b
    """
    # Dijkstra's algorithm (bound is ignored)
    u, v = 0, 1  # go from 0 to 1
    import heapq
    queue = [(0, u, u)]  # distance, node, trail

    trails = {}

    while queue:
        dist, i, j = heapq.heappop(queue)
        if i in trails:
            continue
        trails[i] = j
        if i == v:
            break
        for j in weights[i]:
            if j not in trails:
                heapq.heappush(queue, (dist + weights[i][j], j, i))
    if v in trails:
        rev_path = [v]
        while rev_path[-1] != u:
            rev_path.append(trails[rev_path[-1]])
        return rev_path[::-1]
# assert sat308(sol308())

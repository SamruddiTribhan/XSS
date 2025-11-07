from queue import PriorityQueue

def astar_search(graph, heuristic, start, goal):
    open_list = PriorityQueue()
    open_list.put((0, start))   # (f-score, node)

    came_from = {}              # to store path
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    while not open_list.empty():
        current_f, current_node = open_list.get()

        if current_node == goal:
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start)
            path.reverse()
            return path, g_score[goal]

        for neighbor in graph[current_node]:
            tentative_g = g_score[current_node] + graph[current_node][neighbor]

            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current_node
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic[neighbor]
                open_list.put((f_score, neighbor))

    return None, float('inf')


if __name__ == "__main__":

    graph = {
        'A': {'B': 6, 'F': 3},
        'B': {'A': 6, 'C': 3, 'D': 2},
        'C': {'B': 3, 'D': 1, 'E': 5},
        'D': {'B': 2, 'C': 1, 'E': 8},
        'E': {'C': 5, 'D': 8, 'I': 5, 'J': 5},
        'J': {'E': 5, 'I': 3},
        'I': {'J': 3, 'E': 5, 'H': 2, 'G': 3},
        'H': {'I': 2, 'F': 7},
        'G': {'I': 3, 'F': 1},
        'F': {'A': 3, 'H': 7, 'G': 1}
    }

    heuristic = {
        'A': 10,
        'B': 8,
        'C': 5,
        'D': 7,
        'E': 3,
        'F': 6,
        'G': 5,
        'H': 3,
        'I': 1,
        'J': 0
    }

    start = 'A'
    goal = 'G'

    path, cost = astar_search(graph, heuristic, start, goal)

    print("Shortest Path:", path)
    print("Total Cost:", cost)

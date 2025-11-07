# A* algorithem 2nd assignment

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

    start_node = 'A'
    Goal_node = 'G'

    OPEN = [start_node]  # Add start node to OPEN list
    CLOSED = []

    def astar():
        if not OPEN:
            print('list is empty\nSorry next time!')
            return

        current = OPEN[0]
        print("Current OPEN list:", OPEN)

        if current == start_node:  # Compare with start_node
            f_b = graph['A']['B'] + heuristic['B']
            f_f = graph['A']['F'] + heuristic['F']

            print(f"f(B) = {graph['A']['B']} + {heuristic['B']} = {f_b}")
            print(f"f(F) = {graph['A']['F']} + {heuristic['F']} = {f_f}")

    # CALL THE FUNCTION
    astar()


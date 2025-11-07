# assignment 1: Breadth-First Search (BFS) Implementation

tree={
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F','G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
    }

visited=[]
queue=[]
def bfs(tree, start):
    visited.append(start)
    queue.append(start)

    while queue:
        if queue ==[]:
            print("Queue is empty, BFS completed.")
            return
        node = queue.pop(0)
        print(node)

        for neibor in tree[node]:
            if neibor not in visited:
                visited.append(neibor)
                queue.append(neibor)


# print(tree)
# print(tree['A'])
# print(tree['B'][0])

print("Start BFS from node A")

bfs(tree,'A')
print("Visited nodes:", visited)
print("Queue after BFS:", queue)
print("BFS travel completed.");

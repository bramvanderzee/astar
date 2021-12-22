import sys
from node import Node
import heapq

use_diagonal = True

directions = {
    (0, -1): 'N',
    (1, 0): 'E',
    (0, 1): 'S',
    (-1, 0): 'W',
    (1, -1): 'NE',
    (1, 1): 'SE',
    (-1, 1): 'SW',
    (-1, -1): 'NW'
}

def find_heuristic(to_node, from_node) -> int: # a^2 + b^2
    dx = to_node.x - from_node.x
    dy = to_node.y - from_node.y
    return pow(dx, 2) + pow(dy, 2)

fn = 'input.txt'
if len(sys.argv) > 2:
    fn = sys.argv[1]
    use_diagonal = True if sys.argv[2] == '1' else False
    print("Using diagonals:", use_diagonal)

if len(sys.argv) > 1:
    fn = sys.argv[1]

# Read file 
nodes = [] # map of nodes
xc, yc = 0, 0
start = None
end = None
with open(fn) as f:
    for line in f:
        for c in line.strip():
            n = Node(c, xc, yc)
            nodes.append(n)
            xc += 1

            if c == 'S':
                start = n
            if c == 'E':
                end = n
        xc = 0
        yc += 1

# determine heuristic (pythagoras) max to determine freedom of movement
max_heuristic = 1
if use_diagonal:
    max_heuristic = 2

# Expand nodes list with additional info
for node in nodes:
    if node.c != '#':
        H = find_heuristic(end, node)
        adj = [n for n in nodes if find_heuristic(n, node) <= max_heuristic and n != node and n.c != '#']
        node.add_adj(set(adj))
        node.H = H

def print_path(p: list):
    p.sort(key=lambda n: n.G)
    # print results
    if end not in p:
        print('No path found.')
    else:
        for i in range(1, len(p)):
            n2, n1 = p[i-1], p[i]
            diff = (n1.x - n2.x, n1.y - n2.y)
            print(directions[diff], end=' ')
        print()

def step(state):
    node, path, end = state
    new_path = set(path)
    new_path.add(node)
    if len(path) < node.G:
        node.G = len(new_path)
    else:
        return
    if node == end:
        print_path(list(new_path))
        sys.exit()
    for nxt in sorted(node.adj - new_path):
        step((nxt, new_path, end))

state = (start, set(), end) # current node, path taken, goal
step(state)


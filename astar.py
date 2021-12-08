import sys
from node import Node

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

def find_distance(to_node, from_node, nodes) -> int:
    return 0

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
        G = find_distance(start, node, nodes) # do something with this later
        H = find_heuristic(end, node)
        adj = [n for n in nodes if find_heuristic(n, node) <= max_heuristic and n != node and n.c != '#']
        node.add_adj(adj)
        node.add_cost(G + H)
    
open_nodes = [start]
closed_nodes = []

while len(open_nodes) > 0:
    open_nodes.sort()
    node = open_nodes.pop(0)
    closed_nodes.append(node)
    if node == end:
        break
    open_nodes.extend([n for n in node.adj if n not in closed_nodes and n not in open_nodes])
    
# print results
if end not in closed_nodes:
    print('No path found.')
else:
    for i in range(1, len(closed_nodes)):
        n2, n1 = closed_nodes[i-1], closed_nodes[i]
        diff = (n1.x - n2.x, n1.y - n2.y)
        print(directions[diff], end=' ')
    print()

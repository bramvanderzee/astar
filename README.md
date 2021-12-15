## A star algorithm implementation

### Input 

This algorithm will take a map (consisting of # and .) and find the shortest path from S to E (denoted on this map). A dot (.) denotes an open 'space', while a # represents a wall. This programs takes 0 to 2 arguments. First argument is the filename for the maze (default is 'input.txt'). Second argument is if diagonal steps are allowed (0 or 1, default 1).

### Output

The algorithm will output a set of cardinal directions (N(orth) E(ast) S(outh) W(est)), or any combination of those four, from S(tart) to E(nd).

### Use

`python3 astar.py input.txt 1`

### Complexity

The worst-case complexity of A* is `O(b^d)` where `b` is the branching factor and `d` the depth of the solution. Worst case means the heuristic does not play into account. In our case this means the complexity depends on the settings you give the algorithm. For diagonal search this means a `b`-factor of 8, for non-diagonal search the `b`-factor will be 4. This seems counter-intuitive, but when you take into account the `d`-factor (which will (and can be up to 2 times) smaller for solutions with diagonal steps) this makes more sense. Say for a perfect solution you have to take 5 diagonal steps: for diagonal this means `O(8^5) = 32768`, for non-diagonal this means `O(4^10) = 1048576` (a 32x or 3200% increase). The actual complexity for A* with a heuristic takes into account that the effective branching factor (let's say the average branching factor of a solution). This means in our example the effective branching factor will be much lower (1 for diagonal, because we use euclidian distance for heuristic, 2 for non-diagnonal (one move NE for diagonal is two moves N-E or E-N for non-diagonal)). This gets us the following: `O(1^5) = 1 (!)` for diagonal, `O(2^10) = 1024` for non-diagonal. This number seems logical but is wrong, because in our ideal solution only a single node will be considered for non-diagonals every time (this is because of the ordered queue from Dijkstra). This gets us `O(1^10) = 1`, so `O(1)` complexity for our simple problem.

### TODO:

- Generate random
- test.sh
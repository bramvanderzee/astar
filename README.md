## A star algorithm implementation

### Input 

This algorithm will take a map (consisting of # and .) and find the shortest path from S to E (denoted on this map). A dot (.) denotes an open 'space', while a # represents a wall. This programs takes 0 to 2 arguments. First argument is the filename for the maze (default is 'input.txt'). Second argument is if diagonal steps are allowed (0 or 1).

### Output

The algorithm will output a set of cardinal directions (N(orth) E(ast) S(outh) W(est)), or any combination of those four, from S(tart) to E(nd).

### Use

`python3 astar.py input.txt 1`
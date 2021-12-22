class Node:
    c, x, y, G, H = 0, 0, 0, int(1e9), int(1e9)
    adj = []

    def __init__(self, c, x, y):
        self.c, self.x, self.y = c, x, y
        
    def add_cost(self, G, H):
        self.G = G
        self.H = H
    
    def cost(self) -> int:
        return self.G + self.H

    def add_adj(self, nodes):
        self.adj = nodes

    def __lt__(self, other):
        return self.cost() < other.cost()
        
    def __repr__(self) -> str:
        return str((self.x, self.y))

    def __str__(self) -> str:
        return str([self.c, (self.x, self.y), (self.G, self.H), len(self.adj)])

class Node:
    c, x, y, f = 0, 0, 0, None
    adj = []

    def __init__(self, c, x, y):
        self.c, self.x, self.y = c, x, y
        
    def add_cost(self, cost):
        self.f = cost
    
    def add_adj(self, nodes):
        self.adj = nodes
        
    def __str__(self) -> str:
        return str([self.c, (self.x, self.y), self.f, len(self.adj)])
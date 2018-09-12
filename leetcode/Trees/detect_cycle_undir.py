class DSU(object):
    def __init__(self, nodes):
        self.sets = [self.make_set(node) for node in nodes]

    def make_set(self, x):
        x.p = x
        x.rank = 0
        return x

    def find_set(self, x):
        if x.p != x:
            x.p = self.find_set(x.p)
        return x.p

    def union(self, x, y):
        if x.rank > y.rank:
            y.p = x
        else:
            x.p = y
            if x.rank == y.rank:
                y.rank += 1

    def cycle_detected(self, vertex1, vertex2):
        root1 = self.find_set(self.sets[vertex1])
        root2 = self.find_set(self.sets[vertex2])

        if root1 is root2:
            return True

        self.union(root1, root2)
        return False


class Node(object):
    def __init__(self):
        self.p = None
        self.rank = None


class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        dsu_solver = DSU([Node() for n in xrange(0, len(edges) + 1)])
        for edge in edges:
            if dsu_solver.cycle_detected(edge[0], edge[1]):
                return edge

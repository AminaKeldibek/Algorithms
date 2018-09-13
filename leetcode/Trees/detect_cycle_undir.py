from collections import defaultdict


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


class SolutionDFS(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = defaultdict(list)

        def dfs(node, target):
            if not visited[node - 1]:
                visited[node - 1] = True
                if node == target:
                    return True
                return any(dfs(n, target) for n in graph[node])

        for u, v in edges:
            visited = [False] * len(edges)
            if u in graph.keys() and v in graph.keys() and dfs(u, v):
                return u, v
            graph[u].append(v)
            graph[v].append(u)


def main():
    edges = [[3,4],[1,2],[2,4],[3,5],[2,5]]
    print SolutionDFS().findRedundantConnection(edges)
    print [1, 4]


if __name__ == "__main__":
    main()

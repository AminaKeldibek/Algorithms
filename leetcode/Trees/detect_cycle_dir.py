from collections import defaultdict

class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        self.v1 = 0
        self.v2 = 0
        def find_redun_edge(u, parent):
            if colors_dict[u] == 0:
                colors_dict[u] = 1
                parents_dict[u] = parent
                for v in graph[u]:
                    find_redun_edge(v, u)
                colors_dict[u] = 2
            elif colors_dict[u] == 1:
                self.v1, self.v2 = parent, u
            else:
                self.v1, self.v2 = parents_dict[u], u

        graph = defaultdict(list)
        colors_dict = dict()
        parents_dict = dict()

        for u, v in edges:
            graph[u].append(v)
            colors_dict[u] = 0
            colors_dict[v] = 0

        find_redun_edge(edges[0][0], None)
        return [self.v1, self.v2]


def main():
    edges = [[1,2], [1,3], [2,3]]
    print Solution().findRedundantDirectedConnection(edges)


if __name__ == "__main__":
    main()

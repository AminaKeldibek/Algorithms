from collections import defaultdict

class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        #candidates = []
        parent = dict()
        colors = dict()
        adj_dict = defaultdict(list)

        for u, v in edges:
            colors[u] = 0
            colors[v] = 0
            adj_dict[u].append(v)
            if v in parent:
                #candidates.append(parent[v], v)
                #candidates.append(u, v)
                return [u, v]
            else:
                parent[v] = u

        def findCycle(u, parent):
            if colors[u] == 0:
                colors[u] = 1
                for v in adj_dict[u]:
                    return findCycle(v, u)
            else:
                return [parent, u]

        return findCycle(edges[0][0], None)

        

from collections import defaultdict

class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        def findCycle(u, parent):
            if colors[u] == 0:
                colors[u] = 1
                for v in adj_dict[u]:
                    return findCycle(v, u)
            else:
                return [parent, u]

        candidates = []
        parent = dict()
        colors = dict()
        adj_dict = defaultdict(list)

        for u, v in edges:
            colors[u] = 0
            colors[v] = 0
            adj_dict[u].append(v)
            if v in parent:
                candidates.append((parent[v], v))
                candidates.append((u, v))
            else:
                parent[v] = u

        if not candidates:
            return findCycle(edges[0][0], None)

        adj_dict[candidates[1][0]].remove(candidates[1][1])
        res = findCycle(candidates[0][0], None)

        if not res:
            return candidates[1]
        return candidates[0]

from collections import defaultdict


class SolutionDFS(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = defaultdict(list)
        vertices = set()

        def dfs(node, target, visited):
            if not visited[node - 1]:
                visited[node - 1] = True
                if node == target:
                    return True
                return any(dfs(n, target, visited) for n in graph[node])

        for u, v in edges:
            vertices.add(u)
            vertices.add(v)
            if u in vertices and v in vertices:
                if dfs(u, v, [False] * len(edges)) or dfs(v, u, [False] * len(edges)):
                    return u, v
            graph[u].append(v)


def main():
    edges = [[1,2], [1,3], [2,3]]
    print SolutionDFS().findRedundantConnection(edges)


if __name__ == "__main__":
    main()

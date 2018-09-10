class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        self.memo = {0: [], 1: [TreeNode(0)]}

        def getFBT(N):
            if N not in self.memo:
                self.memo[N] = []
                for i in xrange(0, N):
                    left = getFBT(i)
                    right = getFBT(N - i - 1)
                    for l in left:
                        for r in right:
                            root = TreeNode(0)
                            root.left = l
                            root.right = r
                            self.memo[N].append(root)

            return self.memo[N]

        return getFBT(N)

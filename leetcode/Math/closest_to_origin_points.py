class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        points.sort(key = lambda P: pow(P[0], 2) + pow(P[1], 2))
        return points[:K]

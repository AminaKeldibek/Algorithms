class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        def dp(i):
            if i > days[-1]:
                return 0
            if i in days:
                if i not in cache:
                    cache[i] = min(dp(i + 1) + costs[0], dp(i + 7) + costs[1], dp(i + 30) + costs[2])
                return cache[i]
            else:
                for day in days:
                    if day >= (i + 1):
                        return dp(day)

        cache = dict()

        return dp(1)

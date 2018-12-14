class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        resources = [0, 0]
        for b in bills:
            if b == 5:
                resources[0] += 1
            elif b == 10:
                resources[0] -= 1
                resources[1] += 1
            elif b == 20:
                if resources[1] > 0:
                    resources[1] -= 1
                    resources[0] -= 1
                else:
                    resources[0] -= 3

            if any ([n < 0 for n in resources]):
                return False
        return True

        

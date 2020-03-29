class Solution:
    def find_factor(self, num:int):
        for n in (2, 3, 5):
            if num % n == 0:
                return num / n


    def isUgly(self, num: int) -> bool:
            if num == 0:
                return False

            x = num

            while 1:
                if x in (1, 2, 3, 5):
                    return True
                x = self.find_factor(x)
                if x is None:
                    return False

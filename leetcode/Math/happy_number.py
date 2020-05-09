from typing import Set


class Solution:
    def checkHappyNumber(self, n: int, history: Set[int]):
        if n == 1:
            return True

        new_n = sum(int(digit) ** 2 for digit in str(n))
        if new_n in history:
            return False

        history.add(new_n)
        return self.checkHappyNumber(new_n, history)

    def isHappy(self, n: int) -> bool:
        return self.checkHappyNumber(n, {n})
        

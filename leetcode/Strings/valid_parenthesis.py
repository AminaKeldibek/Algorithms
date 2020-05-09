class Solution:
    def checkValidString(self, s: str) -> bool:
        low_estimate = 0
        high_estimate = 0

        for char in s:
            if char == '(':
                low_estimate += 1
                high_estimate += 1
            elif char == ')':
                low_estimate -= 1
                high_estimate -= 1
            elif char == '*':
                low_estimate -= 1
                high_estimate += 1
            if high_estimate < 0:
                break
            low_estimate = max(low_estimate, 0)

        return low_estimate == 0


        

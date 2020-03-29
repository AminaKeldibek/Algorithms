class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        if len(flowerbed) == 1:
            return (flowerbed[0] == 0 and n < 2) or (flowerbed[0] == 1 and n == 0)

        for i in range (len(flowerbed) - 1):
            if flowerbed[i] == 0:
                if i == 0 and flowerbed[i + 1] == 0:
                    n -= 1
                    flowerbed[i] = 1
                elif flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                    n -= 1
                    flowerbed[i] = 1
            if n <= 0:
                return True

        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            n -= 1
        return n <= 0
                    

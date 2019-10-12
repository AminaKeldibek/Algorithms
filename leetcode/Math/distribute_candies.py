class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        people = [0] * num_people
        candies_left = candies
        for i in range(candies):
            people[i % num_people] += (i + 1)
            candies_left -= (i + 1)
            if candies_left < (i + 2):
                break
        people[(i + 1) % num_people] += candies_left

        return people

        

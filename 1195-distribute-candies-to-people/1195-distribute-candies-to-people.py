class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        
        amounts = [0] * num_people
        idx = 0
        curr = 1
        while candies > 0:
            give = min(candies, curr)
            amounts[idx % num_people] += give
            candies -= give
            curr += 1
            idx += 1
        return amounts

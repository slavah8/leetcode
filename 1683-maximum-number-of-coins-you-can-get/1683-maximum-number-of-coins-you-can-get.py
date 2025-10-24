class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        N = len(piles)
        
        choices = N // 3
        total = 0
        i = 1
        for _ in range(choices):
            total += piles[i]
            i += 2
        
        return total

        
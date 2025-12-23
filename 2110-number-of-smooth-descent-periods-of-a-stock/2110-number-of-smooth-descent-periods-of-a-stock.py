class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        
        n = len(prices)
        run = 1
        total = 1
        for i in range(1, n):
            if prices[i - 1] - prices[i] == 1:
                run += 1
            else:
                run = 1
            total += run
        
        return total

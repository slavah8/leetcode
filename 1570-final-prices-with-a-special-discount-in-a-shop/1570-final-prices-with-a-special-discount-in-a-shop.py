class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        N = len(prices)
        answer = []
        for i, x in enumerate(prices):
            curr = x
            for j in range(i + 1, N):
                if prices[j] <= x:
                    curr -= prices[j]
                    break
            answer.append(curr)
        return answer
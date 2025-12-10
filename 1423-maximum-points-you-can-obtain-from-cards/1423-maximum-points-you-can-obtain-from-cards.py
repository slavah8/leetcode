class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        n = len(cardPoints)
        length = n - k
        total = sum(cardPoints)
        if length == 0:
            return total
        
        l = 0
        INF = 10 ** 10
        best = INF
        window_sum = 0
        for r in range(n):
            x = cardPoints[r]
            window_sum += x

            if r - l + 1> length:
                window_sum -= cardPoints[l]
                l += 1

            if window_sum < best and r - l + 1 == length:
                best = window_sum
            print(best)

        print(best)
        print(total)
        return total - best



class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()

        
        n = len(beans)

        prefix = [0] * (n + 1)
        for i, x in enumerate(beans, 1):
            prefix[i] = prefix[i - 1] + x

        INF = 10 ** 10
        best = INF
        total_sum = prefix[n]
        for i, t in enumerate(beans):
            # make everything to the left zero
            left_cost = prefix[i]

            # make everything to the right t
            right_sum = total_sum - prefix[i]
            right_cnt = n - i 
            right_cost = right_sum - right_cnt * t
            best = min(best, left_cost + right_cost)
        return best






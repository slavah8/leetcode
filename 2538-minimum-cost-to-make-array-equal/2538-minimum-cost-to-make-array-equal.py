class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        pairs = sorted(zip(nums, cost))
        xs = [x for x, _ in pairs]
        ws = [w for _, w in pairs]

        N = len(xs)
        weight_prefix = [0] * (N + 1) # weights only
        sum_prefix = [0] * (N + 1) # (weights * values)

        for i in range(N):
            weight_prefix[i + 1] = weight_prefix[i] + ws[i]
            sum_prefix[i + 1] = sum_prefix[i] + (ws[i] * xs[i])
        print(pairs)
        weight_total = weight_prefix[N]
        half = (weight_total + 1) // 2
        print(weight_prefix)
        print(sum_prefix)
        print(half)
        
        t = xs[-1]
        acc = 0
        for i in range(N):
            acc += ws[i]
            if acc >= half:
                t = xs[i]
                break
        
        total = 0
        for i in range(N):
            total += abs(t - nums[i]) * cost[i]
        return total
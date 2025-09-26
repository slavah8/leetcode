class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        a = sorted(nums)
        N = len(nums)
        prefix = [0] * (N + 1)

        for i in range(N):
            prefix[i + 1] = prefix[i] + a[i]

        total = prefix[N]
        answer = []
        for q in queries:
            k = bisect.bisect_left(a, q)
            
            left_cost = (k * q) - prefix[k]
            right_cost = (total - prefix[k]) - (N - k) * q
            answer.append(left_cost + right_cost)

        return answer

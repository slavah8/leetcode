class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        N = len(nums)
        left_sum = [0] * (N + 1)
        right_sum = [0] * (N + 1)

        for i in range(N):
            left_sum[i + 1] = left_sum[i] + nums[i]

        total = left_sum[N]
        print(total)
        prefix = 0
        for i in range(N):
            prefix += nums[i]
            right_sum[i + 1] = total - prefix
        print(left_sum)
        print(right_sum)

        answer = [0] * N
        for i in range(N):
            answer[i] = abs(left_sum[i] - right_sum[i + 1])
        return answer
        


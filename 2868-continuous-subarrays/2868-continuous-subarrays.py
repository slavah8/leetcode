class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        
        max_dq = deque()
        min_dq = deque()
        left = 0
        total = 0
        for right, x in enumerate(nums):
            while max_dq and x > nums[max_dq[-1]]:
                max_dq.pop()
            max_dq.append(right)
            while min_dq and x < nums[min_dq[-1]]:
                min_dq.pop()
            min_dq.append(right)

            while (nums[max_dq[0]] - nums[min_dq[0]]) > 2 or (nums[max_dq[0]] - nums[min_dq[0]]) < 0:
                if left == max_dq[0]:
                    max_dq.popleft()
                if left == min_dq[0]:
                    min_dq.popleft()
                left += 1
            
            total += right - left + 1
        return total


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        max_deque = deque() # front is always the max of the window
        min_deque = deque() # front is always the min of the window
        left = 0
        best = 0
        for right, x in enumerate(nums):

            while max_deque and nums[max_deque[-1]] < x:
                max_deque.pop()
            max_deque.append(right)
            while min_deque and nums[min_deque[-1]] > x:
                min_deque.pop()
            min_deque.append(right)
            
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                nums_left = nums[left]
                if max_deque and max_deque[0] == left:
                    max_deque.popleft()
                if min_deque and min_deque[0] == left:
                    min_deque.popleft()
                left += 1
            best = max(best, right - left + 1)
        return best

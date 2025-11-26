class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        def is_increasing(arr):
            n = len(arr)
            for i in range(n - 1):
                if arr[i] >= arr[i + 1]:
                    return False
            return True
        
        subarrays = []
        for i in range(n):
            sub = [nums[i]]
            subarrays.append(sub[:])
            for j in range(i + 1, n):
                sub.append(nums[j])
                subarrays.append(sub[:])

        count = 0
        for i in range(n):
            left = i
            
            for j in range(i, n):
                right = j
                removed = nums[left:right + 1]
                new_arr = nums[:left] + nums[right + 1:]
                if is_increasing(new_arr):
                    count += 1
        return count




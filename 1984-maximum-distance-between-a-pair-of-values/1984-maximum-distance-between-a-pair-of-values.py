class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        max_dist = 0
        # Find the farthest valid index to the right where the value is still ≥ x
        def right_most_index(arr, x, low):
            high = len(arr) - 1
            ans = -1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] >= x:
                    low = mid + 1
                    ans = mid
                else:
                    high = mid - 1
            return ans

        for index, x in enumerate(nums1):

            j = right_most_index(nums2, x, index)
            if j != -1:
                max_dist = max(max_dist, j - index)
        return max_dist
            

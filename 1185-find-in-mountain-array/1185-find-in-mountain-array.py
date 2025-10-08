# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        
        length = mountainArr.length()
        low = 1
        high = length - 2
        peak = -1
        # first find the peak
        while low <= high:
            mid = (low + high) // 2
            mid_val = mountainArr.get(mid)
            left_val = mountainArr.get(mid - 1)
            right_val = mountainArr.get(mid + 1)

            if left_val < mid_val and mid_val > right_val: # found peak
                peak = mid
                break
            elif left_val < mid_val < right_val: # sloping up
                low = mid + 1
            elif left_val > mid_val > right_val: # sloping down
                high = mid - 1

        # now that we have the peak we can binary search the left and right of the peak first search the left

        low = 0
        high = peak
        
        while low <= high:
            mid = (low + high) // 2

            if mountainArr.get(mid) == target:
                return mid
            elif mountainArr.get(mid) < target:
                low = mid + 1
            else:
                high = mid - 1
        
        low = peak + 1
        high = length - 1

        while low <= high:
            mid = (low + high) // 2

            if mountainArr.get(mid) == target:
                return mid
            elif mountainArr.get(mid) < target:
                high = mid - 1
            else:
                low = mid + 1
        return -1
        



        
            
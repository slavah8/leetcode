class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        
        length = mountainArr.length()
        low = 1
        high = length - 2
        peak = -1

        # find the peak (neighbors always in-bounds)
        while low <= high:
            mid = (low + high) // 2
            mid_val = mountainArr.get(mid)
            left_val = mountainArr.get(mid - 1)
            right_val = mountainArr.get(mid + 1)

            if left_val < mid_val and mid_val > right_val:  # found peak
                peak = mid
                break
            elif left_val < mid_val < right_val:            # sloping up
                low = mid + 1
            else:                                           # sloping down
                high = mid - 1

        if peak == -1:
            peak = low  # fallback if loop ended without 'break'

        # left side (increasing)
        low = 0
        high = peak
        while low <= high:
            mid = (low + high) // 2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            elif val < target:
                low = mid + 1
            else:
                high = mid - 1
        
        # right side (decreasing) — FLIP directions
        low = peak + 1
        high = length - 1
        while low <= high:
            mid = (low + high) // 2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            elif val < target:
                high = mid - 1      # move LEFT to larger values
            else:  # val > target
                low = mid + 1       # move RIGHT to smaller values

        return -1




        
            
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        
        position.sort()
        def can(d):
            count = 1
            last = position[0]
            for x in position[1:]:
                if x - last >= d:
                    count += 1
                    last = x
                    if count >= m:
                        return True
            return False
        high = position[-1] - position[0]
        low = 1

        while low < high:
            mid = (low + high + 1) // 2

            if can(mid): # increase the distance
                low = mid
            else:
                high = mid - 1
        
        return low



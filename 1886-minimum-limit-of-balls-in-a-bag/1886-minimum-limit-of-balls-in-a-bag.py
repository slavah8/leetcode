class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        
        

        # with the max bag being P
        def feasible(P):
            total = 0
            for x in nums:
                total += math.ceil(x / P) - 1
                if total > maxOperations:
                    return False
            return True


        # trying to find the smallest P penalty bag
        # if P is large its easy to achieve fewer splits
        # if P is small its harder
        high = max(nums)
        low = 1
        while low < high:
            mid = (low + high) // 2
            if feasible(mid):
                high = mid
            else:
                low = mid + 1
        return low


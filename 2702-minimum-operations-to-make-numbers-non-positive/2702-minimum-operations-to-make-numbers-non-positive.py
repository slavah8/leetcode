class Solution:
    def minOperations(self, nums: List[int], x: int, y: int) -> int:
        n = len(nums)
        diff = x - y
        # can we decrement nums in less than or equal to t operations
        def check(t):
            special_needed = 0
            ty = t * y
            for a in nums:
                remain = a - ty
                if remain > 0:
                    # final = a - (t * y) - c * (x - y)
                    # 0 >= a - (t * y) - c * (x - y)
                    # c * (x - y) >= a - (t * y)
                    # c >= (a - (t * y)) / (x - y)
                    # c is how many times the index is special
                    # The minimum number of times this element must be chosen as special
                    c = math.ceil(remain / diff)
                    special_needed += c
                    if special_needed > t:
                        return False
            return special_needed <= t
        
        # how many ops to kill a num even without it being special
        # a - (t * y) <= 0
        # - (t * y) <= - a
        # t * y >= a
        # t >= a / y
        hi = 0
        for a in nums:
            hi = max(hi, math.ceil(a / y))
        
        lo = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid - 1
            else:
                lo = mid + 1
        return lo
                



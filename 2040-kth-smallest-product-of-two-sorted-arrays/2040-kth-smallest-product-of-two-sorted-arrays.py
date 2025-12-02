class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        n1 = len(nums1)
        n2 = len(nums2)

        # helper: how many pairs (i, j) have nums1[i] * nums2[j] <= x ?
        def count(x):
            total = 0
            for a in nums1:
                if a == 0:
                    if x >= 0:
                        total += n2
                elif a > 0:
                    # a * b <= x
                    # b <= x // a
                    limit = x // a
                    total += bisect.bisect_right(nums2, limit)
                else: # a < 0
                    # a * b <= x -> b >= x // a
                    # number of b ≥ limit
                    limit = math.ceil(x / a)
                    idx = bisect.bisect_left(nums2, limit)
                    total += n2 - idx
            return total

        candidates = [
            nums1[0] * nums2[0],
            nums1[0] * nums2[-1],
            nums1[-1] * nums2[0],
            nums1[-1] * nums2[-1]
        ]

        low = min(candidates)
        high = max(candidates)

        while low < high:
            mid = (low + high) // 2
            if count(mid) >= k: # product has to be smaller
                high = mid
            else:
                low = mid + 1
        return low



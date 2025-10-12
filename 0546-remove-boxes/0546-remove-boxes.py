class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        
        N = len(boxes)

        # dp(i, j, k) max amount of points from subarray boxes[i..j] if we already have
        # k extra boxes of the same color as boxes[i] attached to the left
        @lru_cache(None)
        def dp(i, j, k):
            if i > j:
                return 0
            
            p = i
            while p + 1 <= j and boxes[p + 1] == boxes[i]:
                p += 1
            # how many consecutive boxes of the same color starting at boxes[i]
            t = p - i + 1

            # option A :remove now
            res = (k + t) * (k + t) + dp(p + 1, j, 0)

            # option B: defer and try to merge later
            for m in range(p + 1, j + 1):
                if boxes[m] == boxes[i]:
                    # we can merge box m with box i and the left and merge the middle right now
                    res = max(res, dp(p + 1, m - 1, 0) + dp(m, j, k + t))
            
            return res


        return dp(0, N - 1, 0)
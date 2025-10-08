class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10 ** 9 + 7

        A = sorted(nums1)
        total = 0
        best_reduction = 0
        INF = 10 ** 10
        for a, b in zip(nums1, nums2):
            diff = abs(a - b)
            total += diff

            pos = bisect.bisect_left(A, b)
            cand = INF
            if pos < len(A):
                cand = min(cand, abs(A[pos] - b))
            if pos > 0:
                cand = min(cand, abs(A[pos - 1] - b))

            best_reduction = max(best_reduction, diff - cand)
        return (total - best_reduction) % MOD

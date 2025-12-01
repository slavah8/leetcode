class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        n = len(nums)

        diff = defaultdict(int)

        for x in nums:
            diff[x - k] += 1
            diff[x + k + 1] -= 1
        

        sorted_diff = dict(sorted(diff.items()))
        
        pref = 0
        best = 0
        for val, cnt in sorted_diff.items():
            pref += cnt
            best = max(best, pref)
        return best


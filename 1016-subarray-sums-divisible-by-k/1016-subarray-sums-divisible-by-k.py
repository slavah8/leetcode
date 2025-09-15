class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # seen[remainder] = how many prefixes so far had remainder 

        seen = defaultdict(int)
        prefix = 0
        ans = 0
        seen[0] = 1
        for x in nums:
            prefix += x
            ans += seen[prefix % k]
            seen[prefix % k] += 1
        return ans

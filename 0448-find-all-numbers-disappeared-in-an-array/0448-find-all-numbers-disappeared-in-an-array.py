class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        all_nums = set(nums)
        print(all_nums)
        ans = []
        for x in range(1, n + 1):
            if x not in all_nums:
                ans.append(x)
        
        return ans


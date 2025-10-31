class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        
        counts = Counter(nums)
        print(counts)

        ans = []
        for num, cnt in counts.items():
            if cnt == 2:
                ans.append(num)
        return sorted(ans)
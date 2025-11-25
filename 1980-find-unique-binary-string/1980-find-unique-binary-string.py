class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        curr = []
        n = len(nums[0])
        ans = ""
        def backtrack():
            nonlocal ans
            if len(curr) == n:
                num = ''.join(curr[:])
                if num not in nums:
                    ans = num
                return
            

            curr.append('0')
            backtrack()
            curr.pop()

            curr.append('1')
            backtrack()
            curr.pop()
        
        backtrack()
        return ans




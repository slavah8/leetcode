class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        
        bad = []
        parity_arr = []
        for x in nums:
            if x % 2 == 0:
                parity_arr.append(0)
            else:
                parity_arr.append(1)

        for i in range(n - 1):
            if parity_arr[i] == parity_arr[i + 1]:
                bad.append(1)
            else:
                bad.append(0)
        
        print(bad)
        m = len(bad)
        prefix = [0] * n
        for i in range(n - 1):
            prefix[i + 1] = prefix[i] + bad[i]
        print(prefix)

        
        ans = []
        for l, r in queries:
            val = prefix[r] - prefix[l]
            if val == 0:
                ans.append(True)
            else:
                ans.append(False)
        return ans
        
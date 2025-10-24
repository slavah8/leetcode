class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        N = len(nums)
        prefix_max = [0] * (N + 1)

        for i in range(N):
            prefix_max[i + 1] = max(prefix_max[i], nums[i])
        
        print(prefix_max)
        conver = [0] * (N + 1)

        for i in range(N):
            conver[i] = nums[i] + prefix_max[i + 1]
        print(conver)

        arr = [0] * (N + 1)
        for i in range(N):
            arr[i + 1] = arr[i] + conver[i]
        
        return arr[1:]

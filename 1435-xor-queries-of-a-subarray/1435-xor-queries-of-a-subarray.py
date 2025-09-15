class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        N = len(arr)
        prefix_xor = [0] * (N + 1)

        # Therefore, for any subarray [L..R]
        # Everything before L appears in both big XORs and cancels out
        for i in range(N):
            prefix_xor[i + 1] = prefix_xor[i] ^ arr[i]
            
        print(prefix_xor)
        ans = [0] * len(queries)
        for index, (l, r) in enumerate(queries):
            ans[index] = prefix_xor[r + 1] ^ prefix_xor[l]
        
        return ans


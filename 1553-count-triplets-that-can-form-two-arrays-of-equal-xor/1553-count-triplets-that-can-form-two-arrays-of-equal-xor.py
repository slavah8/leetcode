class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        """
        a = b
        arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1] = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]


        """
        ans = 0
        N = len(arr)
        for i in range(N):
            xr = 0
            for k in range(i, N):
                xr ^= arr[k]
                if xr == 0:
                    ans += (k - i)
        return ans
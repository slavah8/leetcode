class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        """
        x ^ a = b
        x ^ a ^ a = b ^ a
        x = b ^ a
        x = arr[i]
        a = pref[i - 1]
        b = pref[i]
        arr[i] = pref[i] ^ pref[i - 1]
        """
        N = len(pref)
        arr = [0] * N
        arr[0] = pref[0]
        for i in range(1, N):
            arr[i] = pref[i] ^ pref[i - 1]
        
        return arr


        
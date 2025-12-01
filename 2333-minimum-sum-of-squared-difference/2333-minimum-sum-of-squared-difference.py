class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        n = len(nums1)

        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]

        K = k1 + k2
        
        max_diff = max(diffs)
        freq = [0] * (max_diff + 1)
        for d in diffs:
            freq[d] += 1
        
        v = max_diff

        while v > 0 and K > 0:
            if freq[v] == 0:
                v -= 1
                continue
            if freq[v] <= K:
                freq[v - 1] += freq[v]
                K -= freq[v]
                freq[v] = 0
                v -= 1
            else: # not enough Ks left to fully remove those differences
                freq[v - 1] += K
                freq[v] -= K
                K = 0
                break

        ans = 0

        for value in range(max_diff + 1):
            if freq[value]:
                ans += (value ** 2) * freq[value]
        
        return ans
            

                
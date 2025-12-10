class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        freq = defaultdict(int)

        for x in arr:
            freq[x] += 1
        
        print(freq)

        freq_sorted = sorted(freq.items(),  key = lambda x: x[1])
        print(freq_sorted)
        unique = len(freq_sorted)
        for val, frq in freq_sorted:
            if frq <= k:
                k -= frq
                unique -= 1
        
        return unique

        
class Solution:
    def maxFreqSum(self, s: str) -> int:
        
        vowels = {'a', 'e', 'i', 'o', 'u'}

        c_max = 0
        v_max = 0

        counts = collections.Counter(s)

        for char, cnt in counts.items():
            if char in vowels:
                v_max = max(v_max, cnt)
            else:
                c_max = max(c_max, cnt)
        return v_max + c_max

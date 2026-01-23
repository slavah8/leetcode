class Solution:
    def countDivisibleSubstrings(self, word: str) -> int:
        n = len(word)

        groups = ["ab", "cde", "fgh", "ijk", "lmn", "opq", "rst", "uvw", "xyz"]

        mapping = [0] * 26
        for val, letters in enumerate(groups, start = 1):
            for ch in letters:
                mapping[ord(ch) - ord('a')] = val
        
        vals = [mapping[ord(ch) - ord('a')] for ch in word]
 
        pref = [0] * (n + 1)

        for i in range(n):
            pref[i + 1] = pref[i] + vals[i]

        total = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                summ = pref[j] - pref[i]
                length = j - i

                if summ % length == 0:
                    total += 1

        return total

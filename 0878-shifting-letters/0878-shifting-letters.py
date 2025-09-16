class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        N = len(s)
        base = ord('a')
        prefix = [0] * (N + 1)
        for index, shift in enumerate(shifts):
            prefix[index + 1] += (prefix[index] + shift) % 26
        
        print(prefix)
        total = prefix[N] % 26
        ans = ""
        for i, char in enumerate(s):
            delta = total - prefix[i]
            new_char = chr((ord(char) - base + delta) % 26 + base)
            ans += new_char
        return ans



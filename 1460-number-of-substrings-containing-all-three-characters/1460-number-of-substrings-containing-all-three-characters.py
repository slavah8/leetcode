class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        N = len(s)
        need = {'a' : 0, 'b': 0, 'c': 0}
        have = 0
        left = 0
        ans = 0
        for right, char in enumerate(s):
            if need[char] == 0:
                have += 1
            need[char] += 1

            while have == 3:
                ans += (N - right)
                left_char = s[left]
                need[left_char] -= 1
                if need[left_char] == 0:
                    have -= 1
                left += 1
        
        return ans
class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        need = [0] * 26

        for char in word2:
            need[ord(char) - ord('a')] += 1
        
        missing = sum(1 for x in need if x > 0)

        have = [0] * 26
        N = len(word1)
        L = 0
        total = 0

        for R, char in enumerate(word1):
            c = ord(char) - ord('a')
            if need[c] > 0:
                have[c] += 1
                if have[c] == need[c]:
                    missing -= 1

            while missing == 0: # shrink to find minimal window
                left_c = ord(word1[L]) - ord('a')
                if need[left_c] == 0:
                    L += 1
                elif have[left_c] > need[left_c]:
                    have[left_c] -= 1 
                    L += 1
                else:
                    break
            
            if missing == 0:
                total += L + 1
        
        return total


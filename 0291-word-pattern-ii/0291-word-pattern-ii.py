class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        
        n = len(pattern)
        m = len(s)
        # i index in pattern
        # j index in s
        def backtrack(i, j, mapping):
            print(i, j, mapping)
            if i == n and j == m:
                return True

            if i >= n:
                return False

            char = pattern[i]
            if char in mapping:
                pat = mapping[char]
                if s[j:j + len(pat)] != pat:
                    return False
                else:
                    if backtrack(i + 1, j + len(pat), mapping):
                        return True
                    else:
                        return False
            
            for k in range(j, m):
                pat = s[j:k + 1]
                if pat in mapping.values():
                    continue
                mapping[char] = pat
                if backtrack(i + 1, k + 1, mapping):
                    return True
                del mapping[char]

            return False

        
        return backtrack(0, 0, defaultdict(str))
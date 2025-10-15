class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        

        def is_prefix_suffix(str1, str2):
            N = len(str1)
            M = len(str2)

            if str2[:N] == str1 and str2[M - N:] == str1:
                return True
            else:
                return False
        N = len(words)
        count = 0
        for i in range(N):
            for j in range(i + 1, N):
                if is_prefix_suffix(words[i], words[j]):
                    count += 1
        return count
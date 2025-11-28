class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        pos = defaultdict(list)
        for i, ch in enumerate(s):
            pos[ch].append(i)

        
        def is_subsequence(word):
            prev = -1
            for ch in word:
                if ch not in pos:
                    return False
                
                index_list = pos[ch] # list of indices we want the earliest one greater than prev

                j = bisect.bisect_right(index_list, prev)
                print(ch)
                print(j)
                if j == len(index_list):
                    return False

                prev = index_list[j]
            return True

        ans = 0
        for w in words:
            if is_subsequence(w):
                ans += 1

        return ans
            
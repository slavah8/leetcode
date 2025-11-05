class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        words = re.findall(r"[a-z]+", paragraph.lower())
        print(words)

        freq = collections.defaultdict(int)

        for w in words:
            freq[w] += 1
        
        for w in banned:
            freq[w] = -100
        
        best_freq = 0
        best = ''
        for w, cnt in freq.items():
            if cnt > best_freq:
                best = w
                best_freq = cnt
        return best

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        
        need_alpha = set(target)
        INF = 10 ** 20
        def count_word(w):
            cnt = [0] * 26
            for ch in w:
                if ch in need_alpha:
                    cnt[ord(ch) - ord('a')] += 1
            return cnt
        
        sticker_cnts = [count_word(w) for w in stickers]

        # target need vector
        need0 = [0] * 26
        for ch in target:
            need0[ord(ch) - 97] += 1
        
        @lru_cache(None)
        def dfs(need_key):

            need = list(need_key)
            if all(x == 0 for x in need):
                return 0

            # choose pivot letter we still need (first nonzero)
            pivot = next((i for i, x in enumerate(need) if x > 0), -1)
            if pivot == -1:
                return 0
            
            best = INF
            for s in sticker_cnts:
                if s[pivot] == 0:
                    continue

                nxt = [0] * 26
                for k in range(26):
                    rem = need[k] - s[k]
                    nxt[k] = rem if rem > 0 else 0
                
                res = dfs(tuple(nxt))
                if res != float('inf'):
                    best = min(best, 1 + res)

            return best

        ans = dfs(tuple(need0))
        return ans if ans != INF else -1

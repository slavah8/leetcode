class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        
        res = []

        for q in queries:
            for w in dictionary:
                ok = False
                mismatches = 0
                for c1, c2 in zip(q, w):
                    if c1 != c2:
                        mismatches += 1
                    if mismatches > 2:
                        break
                if mismatches <= 2:
                    ok = True
                    break
            if ok:
                res.append(q)
        return res
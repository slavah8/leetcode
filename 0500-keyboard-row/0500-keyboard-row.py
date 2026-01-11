class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        count = 0
        keyboard_mapping = {
            1 : "qwertyuiop",
            2 : "asdfghjkl",
            3 : "zxcvbnm"
        }
        res = []

        for w in words:
            lw = w.lower()
            ch = lw[0]
            row = -1
            if ch in "qwertyuiop":
                row = 1
            
            elif ch in "asdfghjkl":
                row = 2
            
            elif ch in "zxcvbnm":
                row = 3
            
            ok = True
            for char in lw[1:]:
                if char not in keyboard_mapping[row]:
                    ok = False
                    break
            if ok:
                res.append(w)
        return res

            
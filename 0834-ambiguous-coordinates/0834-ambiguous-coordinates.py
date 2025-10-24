class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        
        res = []
        t = s[1:-1]
        N = len(t)
        

        def forms(p):
            # case 1 : integer part
            res = []
            if p == '0' or p[0] != '0':
                res.append(p)
            
            for k in range(1, len(p)): # where to put the decimal
                int_part = p[:k]
                frac_part = p[k:]

                # no leading zeroes
                if int_part[0] == '0' and int_part != '0':
                    continue
                # no trailing zero in decimal
                if frac_part[-1] == '0':
                    continue
                
                res.append(int_part + '.' + frac_part)
            return res

        ans = []
        for i in range(1, N):
            left = t[:i]
            right = t[i:]
            left_forms = forms(left)
            right_forms = forms(right)

            print(left_forms)
            print(right_forms)
            for a in left_forms:
                for b in right_forms:
                    ans.append(f'({a}, {b})')
        return ans

                

                




class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        pairs = [
            ("0", "0"),
            ("1", "1"),
            ("6", "9"),
            ("8", "8"),
            ("9", "6"),
        ]

        len_low = len(low)
        len_high = len(high)
        self.ans = 0
        def generate_for_length(L):
            num = [""] * L

            def dfs(left, right):

                if left > right:
                    s = "".join(num)

                    if L == len_low and s < low:
                        return
                    
                    if L == len_high and s > high:
                        return
                    
                    self.ans += 1
                    return

                
                if left == right: # check mid
                    for mid in ["0", "1", "8"]:
                        num[left] = mid
                        s = "".join(num)

                        if L == len_low and s < low:
                            continue
                        
                        if L == len_high and s > high:
                            continue
                        
                        self.ans += 1
                    return
                
                for a, b in pairs:
                    if left == 0 and a == "0" and L > 0:
                        continue
                    
                    num[left] = a
                    num[right] = b
                    dfs(left + 1, right - 1)

            dfs(0, L - 1)
        

        for L in range(len_low, len_high + 1):
            generate_for_length(L)
        return self.ans

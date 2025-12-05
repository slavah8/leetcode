class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        
        res = []
        num = [""] * n
        pairs = [("0", "0"), ("1", "1"), ("6", "9"), ("9", "6"), ("8", "8")]
        def dfs(left, right):


            if left > right:
                res.append(''.join(num))
                return
            
            if left == right: # middle position
                for mid in ["0", "1", "8"]:
                    num[left] = mid
                    res.append("".join(num))
                return

            for a, b in pairs:
                if left == 0 and a == "0":
                    continue
                num[left] = a
                num[right] = b
                dfs(left + 1, right - 1)


        dfs(0, n - 1)
        return res
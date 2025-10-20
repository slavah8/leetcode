class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) <= k:
            return '0'
        N = len(num)
        stack = []
        for x in num:
            x = int(x)
            while stack and k > 0 and stack[-1] > x:
                k -= 1
                stack.pop()
            stack.append(x)
        print(stack)
        while stack and k > 0:
            stack.pop()
            k -= 1
        
        stack = map(str, stack)
        res = ''.join(stack)
        i = 0
        while i < len(res) and res[i] == '0':
            i += 1
        
        res = res[i:]
        return res if res else '0'

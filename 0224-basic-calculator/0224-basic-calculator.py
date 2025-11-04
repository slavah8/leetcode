class Solution:
    def calculate(self, s: str) -> int:
        
        res = 0 # running result at current level
        sign = 1
        stack = []
        num = 0


        def flush_number():
            nonlocal res, sign, num
            if num != 0:
                res += sign * num
                num = 0
        i = 0
        while i < len(s):
            ch = s[i]

            if ch.isdigit():
                num = num * 10 + (ord(ch) - ord('0'))
            
            elif ch == '+' or ch == '-':
                flush_number()
                sign = 1 if ch == '+' else -1
            
            elif ch == '(':
                stack.append((res, sign))
                res = 0
                sign = 1
                num = 0
            
            elif ch == ')':
                flush_number()
                sub = res # Capture that inner value:
                prev_res, prev_sign = stack.pop() # previous result and then add it to whatever is inside this parentheses
                res = prev_res + prev_sign * sub
            
            i += 1 # skip white spaces
        flush_number()
        return res


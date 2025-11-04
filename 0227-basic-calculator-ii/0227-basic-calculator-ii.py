class Solution:
    def calculate(self, s: str) -> int:
        
        stack = []
        num = 0
        last_op = '+'

        def apply(op, val):
            if op == "+":
                stack.append(val)
            elif op == '-':
                stack.append(-val)
            elif op == '*':
                stack.append(stack.pop() * val)
            else: # /
                a = stack.pop()
                stack.append(int(a / val))



        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + (ord(ch) - ord('0'))
            
            elif ch in '+-*/':
                apply(last_op, num)
                num = 0
                last_op = ch
        print(stack)
        apply(last_op, num)
        return sum(stack)


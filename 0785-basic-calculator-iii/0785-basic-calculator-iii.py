class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        i = 0

        def parse_level():
            nonlocal i
            stack = []
            num = 0
            last_op = '+'
            def apply(op, val):
                if op == '+':
                    stack.append(val)
                elif op == '-':
                    stack.append(-val)
                elif op == '*':
                    stack.append(stack.pop() * val)
                else:
                    a = stack.pop()
                    stack.append(int(a / val))


            while i < n:
                ch = s[i]
                print(stack)
                if ch == ' ':
                    i += 1
                    continue

                if ch.isdigit():
                    num = num * 10 + (ord(ch) - ord('0'))
                    i += 1
                    continue

                elif ch == '(':
                    i += 1
                    num = parse_level()
                    continue # do not advance i here parsing ends at the matching ')'

                elif ch in '+-*/' or ch == ')':
                    apply(last_op, num)
                    last_op = ch if ch in '+-*/' else last_op
                    num = 0
                    i += 1
                    if ch == ')':
                        return sum(stack)
                    continue
                
                i += 1
            apply(last_op, num)
            return sum(stack)
        return parse_level()
                



                
                
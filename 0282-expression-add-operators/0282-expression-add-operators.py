class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        res = []
        def backtrack(i, curr_expr, curr_sum, last_num):
            # we can insert either +, -, or *
            if i == n:
                if curr_sum == target:
                    res.append(''.join(curr_expr[:]))
                return
            
        
            if len(curr_expr) == 0 or not curr_expr[-1].isdigit():
                # append a digit

                operator = curr_expr[-1] if curr_expr else '^'
                for j in range(i, n):
                    if j > i and num[i] == '0':
                        break

                    x = int(num[i:j + 1])
                    if operator == '+':
                        new_sum = curr_sum + x
                        curr_expr.append(str(x))
                        backtrack(j + 1, curr_expr, new_sum, x)
                        curr_expr.pop()
                    
                    elif operator == '*':
                        new_sum = curr_sum - last_num + last_num * x
                        curr_expr.append(str(x))
                        backtrack(j + 1, curr_expr, new_sum, last_num * x)
                        curr_expr.pop()

                    elif operator == '-':
                        new_sum = curr_sum - x
                        curr_expr.append(str(x))
                        backtrack(j + 1, curr_expr, new_sum, -x)
                        curr_expr.pop()
                    else:
                        curr_expr.append(str(x))
                        backtrack(j + 1, curr_expr, curr_sum + x, x)
                        curr_expr.pop()
            else:
                # append an operator
                for operator in ('*', '+', '-'):
                    curr_expr.append(operator)
                    backtrack(i, curr_expr, curr_sum, last_num) 
                    curr_expr.pop()  
                    
        backtrack(0, [], 0, 0)
        return res
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        
        def calc(N):
            if N < 0:
                return 0

            digits = list(map(int, str(N)))
            L = len(digits)
            NONE = 10

            @lru_cache(None)
            def dp(pos, tight, started, last, secondLast):
                # # returns (countNumbers, sumWaviness)
                if pos == L:
                    return 1, 0
                
                limit = digits[pos] if tight else 9

                total_cnt = 0
                total_sum = 0

                for d in range(limit + 1):
                    tight2 = tight and (d == limit)

                    if not started and d == 0:
                        cnt_child, sum_child = dp(pos + 1, tight2, False, NONE, NONE)
                        total_cnt += cnt_child
                        total_sum += sum_child
                        continue
                    
                    if not started:
                        # start number now
                        cnt_child, sum_child = dp(pos + 1, tight2, True, d, NONE)
                        total_cnt += cnt_child
                        total_sum += sum_child
                        continue
                    
                    # already started, we are appending digit d
                    inc = 0
                    if secondLast != NONE:
                        if last > d and last > secondLast:
                            inc = 1
                        elif last < d and last < secondLast:
                            inc = 1
                    
                    cnt_child, sum_child = dp(pos + 1, tight2, True, d, last)
                    total_cnt += cnt_child
                    total_sum += inc * cnt_child + sum_child
                return total_cnt, total_sum

            return dp(0, True, False, NONE, NONE)[1]
        return calc(num2) - calc(num1 - 1)

    
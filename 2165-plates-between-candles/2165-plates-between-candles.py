class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        N = len(s)
        prefix = [0] * (N + 1)
        for i, char in enumerate(s):
            prefix[i + 1] = prefix[i] + (1 if char == "*" else 0)
        
        left_candle = [-1] * N
        last = -1
        for i, char in enumerate(s):
            if char == "|":
                last = i
            left_candle[i] = last
        print(left_candle)
        right_candle = [-1] * N
        nxt = -1
        for i in range(N - 1, -1, -1):
            if s[i] == '|':
                nxt = i
            right_candle[i] = nxt
        print(right_candle)

        answer = [0] * len(queries)

        for i, (left, right) in enumerate(queries):
            cL = right_candle[left]
            cR = left_candle[right]
            print(cL, cR)
            if cL == -1 or cR == -1 or cL >= cR:
                answer[i] = 0
            else:
                plates = prefix[cR] - prefix[cL]
                answer[i] = plates
        return answer


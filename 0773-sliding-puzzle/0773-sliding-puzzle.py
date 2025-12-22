class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        
        start = ''.join(str(x) for row in board for x in row)
        target = "123450"

        if start == target:
            return 0
        
        adj = {
            0 : [1, 3],
            1 : [0, 2, 4],
            2 : [1, 5],
            3 : [0, 4],
            4 : [1, 3, 5],
            5 : [2, 4]
        }

        queue = deque([(start, 0)])
        seen = {start}
        while queue:
            state, moves = queue.popleft()

            zero_idx = state.index('0')
            for nxt in adj[zero_idx]:
                lst = list(state)
                lst[nxt], lst[zero_idx] = lst[zero_idx], lst[nxt]
                if ''.join(lst) == target:
                    return moves + 1
                if ''.join(lst) not in seen:
                    queue.append((''.join(lst), moves + 1))
                    seen.add(''.join(lst))
        return -1

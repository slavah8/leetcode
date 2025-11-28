class Node:
    def __init__(self, length = 0, pref_char = "", pref_len = 0, suff_char = "", suff_len = 0, best = 0):
        self.length = length
        self.pref_char = pref_char
        self.pref_len = pref_len
        self.suff_char = suff_char
        self.suff_len = suff_len
        self.best = best

def make_leaf(ch):
    return Node(
        length = 1,
        pref_char = ch,
        pref_len = 1,
        suff_char = ch,
        suff_len = 1,
        best = 1
    )

def merge(left, right):
    if left.length == 0:
        return right
    if right.length == 0:
        return left
    
    res = Node()
    res.length = left.length + right.length
    
    # prefix
    res.pref_char = left.pref_char
    res.pref_len = left.pref_len
    if left.pref_len == left.length and left.pref_char == right.pref_char:
        res.pref_len = left.length + right.pref_len
    
    # suffix
    res.suff_char = right.suff_char
    res.suff_len = right.suff_len
    if right.suff_len == right.length and right.suff_char == left.suff_char:
        res.suff_len = right.length + left.suff_len
    
    res.best = max(left.best, right.best)
    if left.suff_char == right.pref_char:
        res.best = max(res.best, left.suff_len + right.pref_len)
    
    return res
class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        chars = list(s)

        tree = [Node() for _ in range(4 * n)]

        def build(idx, l, r):
            if l == r:
                tree[idx] = make_leaf(chars[l])
                return
            
            mid = (l + r) // 2
            build(idx * 2, l, mid)
            build(idx * 2 + 1, mid + 1, r)
            tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1])
        
        def update(idx, l, r, pos, ch):
            if l == r:
                tree[idx] = make_leaf(ch)
                return

            mid = (l + r) // 2
            if pos <= mid:
                update(idx * 2, l, mid, pos, ch)
            else:
                update(idx * 2 + 1, mid + 1, r, pos, ch)
            tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1])
        
        build(1, 0, n - 1)
        ans = []
        for c, i in zip(queryCharacters, queryIndices):
            if chars[i] != c:
                chars[i] = c
                update(1, 0, n - 1, i, c)
            ans.append(tree[1].best)
        return ans 

        
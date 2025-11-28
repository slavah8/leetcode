class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        
        # tree[idx] = number of empty positions in the segment [l, r]
        n = len(people)
        size = n * 4
        tree = [0] * size # # tree[idx] = number of empty slots in that segment
        people.sort(key = lambda x: (x[0], -x[1]))

        def build(idx, left, right):
            if left == right:
                tree[idx] = 1
                return
            mid = (left + right) // 2
            build(idx * 2, left, mid)
            build(idx * 2 + 1, mid + 1, right)
            tree[idx] = tree[idx * 2] + tree[idx * 2 + 1]


        def update(idx, left, right, pos):
            if left == right:
                tree[idx] = 0
                return
            
            mid = (left + right) // 2
            if pos <= mid:
                update(idx * 2, left, mid, pos)
            else:
                update(idx * 2 + 1, mid + 1, right, pos)

            tree[idx] = tree[idx * 2] + tree[idx * 2 + 1]
        
        def find_kth(idx, l, r, k):
            if l == r:
                return l
            left_sum = tree[idx * 2]
            mid = (l + r) // 2
            if left_sum >= k:
                return find_kth(idx * 2, l, mid, k)
            else:
                return find_kth(idx * 2 + 1, mid + 1, r, k - left_sum)
            
        
        build(1, 0, n - 1)
        result = [None] * n

        for h, k in people:

            pos = find_kth(1, 0, n - 1, k + 1)
            result[pos] = [h, k]
            update(1, 0, n - 1, pos)
        return result
            

class Solution:
    def pathSum(self, nums: List[int]) -> int:
        
        node_map = defaultdict(int)
        root = None
        max_depth = 0
        for num in nums:
            x = str(num)
            node = int(x[2])
            pos = int(x[1])
            depth = int(x[0])
            if depth > max_depth:
                max_depth = depth
            if pos == 1 and depth == 1:
                root = int(node)
            node_map[(depth, pos)] = node
        
        print(node_map)
        total = 0
        def dfs(depth, pos, acc):
            nonlocal total
            node = node_map[(depth, pos)]
            acc += node
            left = (depth + 1, 2 * pos - 1)
            right = (depth + 1, 2 * pos)
            has_left = left in node_map
            has_right = right in node_map
            if not has_left and not has_right:
                total += acc
                return

            if has_left:
                dfs(depth + 1, 2 * pos - 1, acc)
            if has_right:
                dfs(depth + 1, 2 * pos, acc)

        
        dfs(1, 1, 0)
        return total
        
        
        


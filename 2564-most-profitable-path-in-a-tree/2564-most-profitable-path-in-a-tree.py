class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        INF = 10 ** 10
        alice_time = [0] * n
        bob_time = [INF] * n # INF if bob doesnt visit the node
        def dfs(u, parent, depth):
            
            alice_time[u] = depth
            dist_to_bob = 0 if u == bob else -1
            for v in graph[u]:
                if v == parent:
                    continue
                
                child_dist = dfs(v, u, depth + 1)
                if child_dist != -1:
                    dist_to_bob = child_dist + 1
            
            if dist_to_bob != -1:
                bob_time[u] = dist_to_bob
            return dist_to_bob

            


        dfs(0, -1, 0)
        print(alice_time)
        print(bob_time)

        gain = [0] * n
        for i in range(n):
            if bob_time[i] > alice_time[i]:
                gain[i] = amount[i]
            elif bob_time[i] == alice_time[i]:
                gain[i] = amount[i] // 2
            else:
                gain[i] = 0

        best = -INF
        def dfs_profit(u, parent, cur_sum):
            nonlocal best
            is_leaf = True
            for v in graph[u]:
                if v == parent:
                    continue
                is_leaf = False
                dfs_profit(v, u, cur_sum + gain[v])
            if is_leaf:
                best = max(best, cur_sum)
                
        
        dfs_profit(0, -1, gain[0])
        return best
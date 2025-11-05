class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        n = len(servers)
        m = len(tasks)
        available = [(weight, idx) for idx, weight in enumerate(servers)] # available servers
        heapify(available) # (weight, idx)

        busy = [] # (free_time, server_idx)
        ans = [0] * m
        time = 0

        for i, t in enumerate(tasks):
            if time < i:
                time = i
            
            while busy and busy[0][0] <= time:
                end, server = heapq.heappop(busy)
                heapq.heappush(available, (servers[server], server))
            
            if available:
                weight, server = heapq.heappop(available)
                heapq.heappush(busy, (time + t, server))
                ans[i] = server
            else:
                free_time, server_idx = heapq.heappop(busy)
                time = free_time

                heapq.heappush(available, (servers[server_idx], server_idx))
                while busy and busy[0][0] <= time:
                    ft, s2 = heapq.heappop(busy)
                    heapq.heappush(available, (servers[s2], s2))

                w, srv = heapq.heappop(available)
                heapq.heappush(busy, (time + t, srv))
                ans[i] = srv
            if time < i + 1:
                time = i + 1

            
        return ans


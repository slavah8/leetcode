class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        N = len(rooms)
        visited = [False] * N
        visited[0] = True
        def dfs(node):

            visited[node] = True
            for nei in rooms[node]:
                if not visited[nei]:
                    dfs(nei)
        
        dfs(0)
        print(visited)
        for room in visited:
            if not room:
                return False
        return True
        
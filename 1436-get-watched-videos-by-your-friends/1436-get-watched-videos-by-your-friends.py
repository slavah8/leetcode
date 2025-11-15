class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], ID: int, level: int) -> List[str]:
        
        friend_map = defaultdict(list)

        for node, neighbors in enumerate(friends):
            for nei in neighbors:
                friend_map[node].append(nei)
                
        
        print(friend_map)
        queue = deque([(ID, 0)]) # (ID, level)
        videos_map = defaultdict(int) # video : # of times watched
        visited = set()
        while queue:
            ID, lvl = queue.popleft()
            if ID in visited:
                continue
                
            visited.add(ID)
            if lvl > level:
                continue
            

            for video in watchedVideos[ID]:
                if lvl == level:
                    videos_map[video] += 1

            for neighbor in friend_map[ID]:
                if neighbor not in visited:
                    queue.append((neighbor, lvl + 1))
        
        result = []
        
        return sorted(videos_map.keys(), key=lambda v: (videos_map[v], v))


            


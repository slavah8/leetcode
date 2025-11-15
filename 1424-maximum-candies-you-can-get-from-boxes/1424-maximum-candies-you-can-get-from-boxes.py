class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)
        total = 0
        future_boxes = set()
        queue = deque()
        have_keys = set()
        visited = [False] * n
        for box in initialBoxes:
            future_boxes.add(box)
            if status[box] == 1:
                queue.append(box)
        
        
        while queue:
            box = queue.popleft()
            if visited[box]:
                continue
            visited[box] = True
            total += candies[box]
            # collect keys from this box
            for k in keys[box]:
                if k not in have_keys:
                    have_keys.add(k)
                    # if we already have this box and it's closed, now we can open it
                    if k in future_boxes and not visited[k]:
                        queue.append(k)
            # collect boxes contained in this box            
            for b in containedBoxes[box]:
                if b not in future_boxes:
                    future_boxes.add(b)
                if not visited[b] and (b in have_keys or status[b] == 1):
                    queue.append(b)



        
        return total


        

                
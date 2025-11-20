class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        INF = 10 ** 10
        start_x, start_y = start
        target_x, target_y = target
        pq = [(0, start_x, start_y)] # (cost, x, y)
        cost = defaultdict(lambda: INF)  # {(x, y) : min_cost}
        cost[(start_x, start_y)] = 0
        
        while pq:
            cur_cost, x, y = heapq.heappop(pq)

            if x == target_x and y == target_y:
                return cur_cost
            
            for road in specialRoads:
                x1, y1, x2, y2, special_cost = road
                get_to_road_cost = abs(x - x1) + abs(y - y1)
                if cost[(x1, y1)] > get_to_road_cost + cur_cost:
                    cost[(x1, y1)] = get_to_road_cost + cur_cost
                    heapq.heappush(pq, (cur_cost + get_to_road_cost, x1, y1))
                if x1 == x and y1 == y and cost[(x2, y2)] > special_cost + cur_cost:
                    cost[(x2, y2)] = special_cost + cur_cost
                    heapq.heappush(pq, (special_cost + cur_cost, x2, y2))
            
            target_cost = abs(target_x - x) + abs(target_y - y)
            if cost[(target_x, target_y)] > target_cost + cur_cost:
                cost[(target_x, target_y)] = target_cost + cur_cost
                heapq.heappush(pq, (target_cost + cur_cost, target_x, target_y))
            
            
            
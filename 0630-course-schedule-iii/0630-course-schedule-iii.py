class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key = lambda x: x[1]) # sort by deadlines

        print(courses)

        t = 0 # days 
        heap = []
        for d, last in courses:
            heapq.heappush(heap, -d)
            t += d
            if t > last:
                longest = -heapq.heappop(heap)
                t -= longest
        return len(heap)
            
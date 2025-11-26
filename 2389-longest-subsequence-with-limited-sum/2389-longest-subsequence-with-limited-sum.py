class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        m = len(queries)
        answer = []
        nums.sort()
        for limit in queries:
            curr_sum = 0
            size = 0
            for x in nums:
                if curr_sum + x > limit:
                    break
                curr_sum += x
                size += 1
            answer.append(size)
        
        return answer

            


                







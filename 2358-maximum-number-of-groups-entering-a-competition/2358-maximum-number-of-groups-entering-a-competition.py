class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        
        # binary search the number of groups and see if it meets the conditions

        n = len(grades)
        grades.sort()
        def check(groups):
            
            i = 0
            prev_sum = 0
            curr_sum = 0
            curr_size = 0
            prev_size = 0
            num_groups = 0
            while i < n:
                x = grades[i]
                curr_sum += x
                curr_size += 1
                if curr_sum > prev_sum and curr_size > prev_size: # we can make a new group
                    prev_sum = curr_sum
                    curr_sum = 0
                    prev_size = curr_size
                    curr_size = 0
                    num_groups += 1
                    i += 1
                else:
                    # need bigger sum or or more students
                    i += 1
            
            return num_groups >= groups
    
        
        low = 1
        high = len(grades)
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                low = mid + 1
                ans = mid
            else:
                high = mid - 1
        return ans







            
        
        print(grades)


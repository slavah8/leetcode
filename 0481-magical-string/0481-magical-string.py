class Solution:
    def magicalString(self, n: int) -> int:
        s = '122'

        curr_num = '1' 
        flip = 0 # if flip = 0 then curr_num is 1

        
        size = 3
        i = 2 # pointer in s
        occurrences = int(s[2])
        while size < n:
            if size + occurrences > n:
                occurrences = n - size
            s += (curr_num * occurrences)
            i += 1
            size = len(s)
            occurrences = int(s[i])
            if flip == 0:
                curr_num = '2'
                flip = 1
            elif flip == 1:
                curr_num = '1'
                flip = 0
        return s.count('1')
            
            
            

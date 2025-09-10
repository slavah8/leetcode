class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        list1 = [] # positive integers
        list2 = [] # negative integers

        for x in nums:
            if x < 0:
                list2.append(x)
            else:
                list1.append(x)
        
        N = len(list1)
        M = len(list2)
        i = 0
        j = 0
        result = []

        print(list1)
        print(list2)
        positive = True
        while i < N or j < M:
            if positive:
                result.append(list1[i])
                i += 1
                positive = not positive
            else:
                result.append(list2[j])
                j += 1
                positive = not positive
        
        return result



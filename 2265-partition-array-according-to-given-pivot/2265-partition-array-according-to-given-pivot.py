class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        list1 = []
        list2 = []
        list3 = []

        for x in nums:
            if x < pivot:
                list1.append(x)
            elif x == pivot:
                list2.append(x)
            else:
                list3.append(x)
        
        return list1 + list2 + list3
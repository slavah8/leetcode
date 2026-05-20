class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        n = len(A)
        m = len(B)

        counts1 = defaultdict(int)
        counts2 = defaultdict(int)
        result = []
        for i in range(n):

            counts1[A[i]] += 1
            counts2[B[i]] += 1

            curr = 0
            for num1, cnt2 in counts1.items():
                for num2, cnt2 in counts2.items():
                    if num1 == num2:
                        curr += 1
            
            result.append(curr)
        
        return result





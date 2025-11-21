class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        total = 0
        numbers = set()
        num = []
        n = len(digits)
        used = set() # used indices
        def recurse():
            print(num)
            if len(num) > 3:
                return

            if len(num) == 3:
                x = int(''.join(num))
                if x % 2 == 0 and num[0] != '0':
                    print(num)
                    
                    numbers.add(x)
                return
                
             
            for i, x in enumerate(digits):
                if i not in used:
                    num.append(str(x))
                    used.add(i)
                    recurse()
                    num.pop()
                    used.remove(i)

        recurse()
        print(numbers)
        return len(numbers)



            
        
        

        
        







            



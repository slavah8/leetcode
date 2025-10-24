class ProductOfNumbers:

    def __init__(self):
        self.stream = []
        self.prefix_prod = []

    def add(self, num: int) -> None:
        self.stream.append(num)
        
        
        if num == 0:
            self.prefix_prod = []
            return
        if len(self.prefix_prod) == 0:
            self.prefix_prod.append(num)
            return
        x = self.prefix_prod[-1] * num
        self.prefix_prod.append(x)
        

        

        

    def getProduct(self, k: int) -> int:
        N = len(self.prefix_prod)
        if N == k:
            return int(self.prefix_prod[N - 1])
        if k >= len(self.prefix_prod):
            return 0
        else:
            return int(self.prefix_prod[N - 1] / self.prefix_prod[N - k - 1])
        
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
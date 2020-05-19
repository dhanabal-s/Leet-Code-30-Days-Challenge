class StockSpanner:

    def __init__(self):
        self.stockList = [0]
        self.spanCount = [0]

    def next(self, price: int) -> int:
        spanCount = 1
        while(self.stockList and self.stockList[-1]<=price):
            spanCount += self.spanCount.pop()
            self.stockList.pop()
        self.stockList.append(price)
        self.spanCount.append(spanCount)
        return spanCount
        
Time Complexity: O(Q).  O(Q), where QQ is the number of calls to StockSpanner.next. 
                        In total, there are Q pushes to the stack, and at most Q pops.

Space Complexity: O(Q).
  

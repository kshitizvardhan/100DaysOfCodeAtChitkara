class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        Prices=sorted(prices)
        minCost = Prices[0] + Prices[1]
        if minCost <= money:
            return money - minCost
        else:
            return money 
        

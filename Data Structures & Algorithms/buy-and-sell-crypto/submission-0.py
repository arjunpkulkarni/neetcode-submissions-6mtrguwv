class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # no prices -> no profit (base case)
        if not prices:
            return 0
        
        # prefix: smallest price so far
        min_price = prices[0] 

        # suffix idea: best profit seen so far
        max_profit = 0

        for price in prices:
            # update prefix (min so far)
            min_price = min(min_price, price)

            # calculate profit if sold today
            profit = price - min_price

            # update suffix (best profit so far)
            max_profit = max(max_profit, profit)

        return max_profit

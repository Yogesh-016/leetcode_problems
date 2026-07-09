class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize the minimum price to a very large number 
        # and the maximum profit to 0
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # Update the minimum price seen so far
            if price < min_price:
                min_price = price
            # Calculate profit if sold today and update max_profit if it's higher
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit
        
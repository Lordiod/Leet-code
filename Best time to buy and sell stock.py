#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
#Difficulty = Easy

def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
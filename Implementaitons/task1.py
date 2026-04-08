"""
1. The Basic Price Action Tracker
Concepts: Lists, for loops, variable tracking, conditional logic (if/else)
The Premise: You are analyzing a sequence of daily closing prices for a stock, and you want to extract some basic statistics about how the stock behaved over that period.
The Task: Write a function that takes a list of prices: prices = [105, 108, 107, 110, 115, 112, 118].

Iterate through the list and compare each day's price to the previous day's price.

Count the total number of "Green Days" (price went up) and "Red Days" (price went down or stayed flat).

Keep track of the largest single-day price jump (e.g., going from 110 to 115 is a jump of +5).

Output: Print the total Green Days, total Red Days, and the value of the largest jump.
"""

prices = [105, 108, 107, 110, 115, 112, 118]

def tracker(prices):
    j=1
    green=0
    red=0
    max_green=0
    for i in range(len(prices)-1):
        if prices[j]-prices[i] <=0:
            red +=1
            j+=1
        else:
            green +=1 
            if prices[j]-prices[i] > max_green:
                max_green = prices[j]-prices[i]
            j+=1
    return red, green, max_green

print(tracker(prices))


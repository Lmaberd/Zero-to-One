"""
1. The Simple SMA Backtester
Concepts: State management, sliding windows, tracking variables over time.
The Premise: You are testing a simple algorithmic trading strategy on a single stock. The strategy is based on a Simple Moving Average (SMA).
The Task:
Write a function that takes a list of daily prices and an integer window_size (e.g., 3 days).

prices = [100, 102, 101, 105, 108, 107, 110, 108, 105]

Calculate the moving average for the given window size. (For day 3, average days 1, 2, 3. For day 4, average days 2, 3, 4).

The Strategy:

If today's price crosses above the moving average, and you don't own the stock, BUY 1 share.

If today's price crosses below the moving average, and you currently own the stock, SELL 1 share.

Keep track of your total profit or loss from these trades. Assume you start with $0 and can have a negative cash balance temporarily.

Output: Return the total number of trades executed and the final realized profit/loss.
"""

prices = [100, 102, 101, 105, 108, 107, 110, 108, 105]

def strategy(prices, days):

    pnl = 0
    total_trades = 0
    owned = False
    for i in range(days-1,len(prices)):
        j=i-days+1
        moving_avg = sum(prices[j:i+1])/days

        if owned:
            pnl += prices[i] - prices[i-1]

        if prices[i] > moving_avg and not owned:
            total_trades += 1
            owned = True
        elif prices[i] < moving_avg and owned:
            total_trades += 1
            owned = False

    return pnl, total_trades

print(strategy(prices,3))


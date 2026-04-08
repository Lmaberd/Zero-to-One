"""
3. The Simple Portfolio Rebalancer
Concepts: Dictionaries (Hash Maps), basic math, iterating over keys and values
The Premise: You have a small portfolio of assets, and you want to rebalance it so that your wealth is distributed exactly according to a target percentage.
The Task:
Write a function that takes two dictionaries:

current_holdings = {"Stock_A": 400, "Stock_B": 500, "Cash": 100} (These are dollar amounts).

target_allocation = {"Stock_A": 0.50, "Stock_B": 0.30, "Cash": 0.20} (These are percentages that add up to 1.0).

First, calculate the total value of the entire portfolio.

Next, calculate exactly how much money should be in each asset based on the target_allocation.

Output: Return a new dictionary showing the difference—how much of each asset you need to buy or sell. For example, if you currently have $400 of Stock_A, but the target says you should have $500, the output should show {"Stock_A": +100}.
"""

current_holdings = {"Stock_A": 400, "Stock_B": 500, "Cash": 100}
target_allocation = {"Stock_A": 0.50, "Stock_B": 0.30, "Cash": 0.20}

def rebalancer(current_holdings, target_allocation):
    rebalanced = {}
    total = sum(current_holdings.values())

    for key in target_allocation.keys():
        if total*target_allocation[key] == current_holdings[key]:
            continue
        else:
            rebalanced[key] = total*target_allocation[key] - current_holdings[key]
    
    return rebalanced

print(rebalancer(current_holdings, target_allocation))
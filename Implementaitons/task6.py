"""
The Financial Entity Graph

Concepts: Graphs, Adjacency Lists, Breadth-First Search (BFS) or Depth-First Search (DFS).

The Premise: You are building a high-level relationship graph to map out how different SQL database tables are connected. You need to verify if an AI agent can trace a path from one specific data table to another through shared foreign keys.

The Task:
Write a function can_reach(edges, start_node, target_node).

You are given a list of bidirectional relationships:
edges = [("Users", "Transactions"), ("Transactions", "Merchants"), ("MarketData", "Tickers")]

First, transform this flat list of edges into an Adjacency List (a dictionary where each key is a table, and its value is a list of all tables it directly connects to).

Then, write a search algorithm to determine if there is a valid path from the start_node to the target_node.

Example: can_reach(edges, "Users", "Merchants") should return True. can_reach(edges, "Users", "MarketData") should return False.
"""

edges = [("Users", "Transactions"), ("Transactions", "Merchants"), ("MarketData", "Tickers")]

def can_reach(edges, start_node, target_node):
    adj_list = {}

    # To unpack list e.g. list = [(x,y), (a,b)] use "for r1, r2 in edges:" where r1 = x and r2 = y in first iteration
    for r1, r2 in edges:
        # Add key if it doesnt exist
        if r1 not in adj_list.keys():
            adj_list[r1] = []
        # Add value if it doesnt exist
        if r2 not in adj_list[r1]:
            adj_list[r1].append(r2)

        # Repeat everything for r2
        if r2 not in adj_list.keys():
            adj_list[r2] = []
        if r1 not in adj_list[r2]:
            adj_list[r2].append(r1)

    
    # BFS

    # Use set because visited should always be unique
    visited = set()
    # .add() is a set method
    visited.add(start_node)

    queue = [start_node]

    while len(queue) > 0:
        current_node = queue.pop(0)
        if current_node == target_node:
            return True
        
        # Add list to queue if not yet visited
        else:
            for i in adj_list[current_node]:
                if i not in visited:
                    queue.append(i)
                    visited.add(i)

    return False



print(can_reach(edges, "Users", "Merchants"))
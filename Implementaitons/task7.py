"""
2. The Microstructure Volume Spike

Concepts: Monotonic Stacks, Arrays, O(N) Time Complexity Optimization.

The Premise: You are analyzing market microstructure data to calculate analytical latency. You have an array representing trade volume tick-by-tick.
For every single tick, you want to know exactly how many ticks you have to wait until you see a volume spike that is strictly greater than the current tick.

The Task:
Write a function wait_times(volumes).
volumes = [70, 72, 68, 65, 75, 71, 76]
For the first volume (70), the next higher volume is 72, which is 1 tick away.

For 72, the next higher volume is 75, which is 3 ticks away.
If a higher volume never occurs (like 76 at the end), the wait time is 0.

The Catch: You cannot use a nested for loop (an O(N^2) solution) because this array could contain millions of ticks.

You must solve this in O(N) time using a Stack. Output: Return an array of wait times: [1, 3, 2, 1, 2, 1, 0].
"""

volumes = [70, 72, 68, 65, 75, 71, 76]


def wait_times(volumes):
    wait_list = [0] * len(volumes)

    stack = []  # Stores index instead of value

    #  enumerate is same as range(len(x)), but gives outputs of (idx, value) e.g. [(0, "apple"), (1, "Banana")]
    for i, vol in enumerate(volumes):

        # While loop to check if current vol > vol of last added index in stack, if true, pop stack and calculate to wait_time, repeat until idx_position value is less than current value
        # Although it is a nested loop, the while loop only runs once every for loop, therefore it is not O(N^2).
        while len(stack) > 0 and vol > volumes[stack[-1]]:
            # store pop() value. pop() defaults to popping value of stack[-1].
            idx_position = stack.pop()
            #  wait_time is the count before the current index
            wait_time = i - idx_position

            wait_list[idx_position] = wait_time

        stack.append(i)
    
    return wait_list

print(wait_times(volumes))



        


        
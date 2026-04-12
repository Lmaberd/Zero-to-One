"""
The Microcontroller Rolling Window
Concepts: Fixed-size data structures, continuous mathematical updates, thresholding.
The Premise: You are programming a small edge-computing device (like a Raspberry Pi Pico) to monitor temperature sensors. Because memory is limited, it can only remember the last N readings at any given time.
The Task:
Create a class called SensorBuffer initialized with a max_size (e.g., 5).

Write an add_reading(value) method. If the buffer has fewer than 5 items, simply add the value. If it already has 5 items, discard the oldest reading to make room for the new one.

Write a get_average() method that returns the average of the current buffer.

The Catch: Add an is_anomaly(value) method. Before adding a new reading to the buffer, check if it is more than 20% higher or lower than the current average of the buffer. 
If it is, return True (and still add it). Otherwise, return False.

Output: A working class where you can feed it a continuous stream of numbers and it will correctly flag anomalies based only on its limited recent memory.
"""

class SensorBuffer():
    # Classes always have an __init__ method, and all methods always have a "self" argument
    def __init__(self, max_size):
        self.max_size = max_size
        # init a list for the buffer
        self.buffer = []


    def add_reading(self, value):
        if len(self.buffer) < self.max_size:
            self.buffer.append(value)
        elif len(self.buffer) >= self.max_size:
            self.buffer.append(value)
            self.buffer.pop(0)
        
    def get_average(self):
        if len(self.buffer) == 0:
            return 0
        
        return sum(self.buffer)/len(self.buffer)

    
    def is_anomaly(self, value):
        if len(self.buffer) == 0:
            self.add_reading(value)
            return False
        
        higher = self.get_average()*1.2
        lower = self.get_average()*0.8
        check = False
        if value > higher or value < lower:
            check = True

        self.add_reading(value)

        return check

sensor = SensorBuffer(max_size=3)

print(sensor.is_anomaly(10)) # False (Buffer was empty)
print(sensor.is_anomaly(10)) # False (Avg is 10)
print(sensor.is_anomaly(10)) # False (Avg is 10)
print(sensor.is_anomaly(25)) # True! (25 is > 12)




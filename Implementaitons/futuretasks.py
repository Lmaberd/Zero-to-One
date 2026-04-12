"""

2. The Microcontroller Rolling Window
Concepts: Fixed-size data structures, continuous mathematical updates, thresholding.
The Premise: You are programming a small edge-computing device (like a Raspberry Pi Pico) to monitor temperature sensors. Because memory is limited, it can only remember the last $N$ readings at any given time.
The Task:
Create a class called SensorBuffer initialized with a max_size (e.g., 5).

Write an add_reading(value) method. If the buffer has fewer than 5 items, simply add the value. If it already has 5 items, discard the oldest reading to make room for the new one.

Write a get_average() method that returns the average of the current buffer.

The Catch: Add an is_anomaly(value) method. Before adding a new reading to the buffer, check if it is more than 20% higher or lower than the current average of the buffer. 
If it is, return True (and still add it). Otherwise, return False.

Output: A working class where you can feed it a continuous stream of numbers and it will correctly flag anomalies based only on its limited recent memory.

3. The Context-Aware Text Chunker
Concepts: String parsing, boundary conditions, building accumulators.
The Premise: You are preparing a raw corporate earnings transcript to be fed into a Large Language Model. The LLM has a strict token limit, so you need to split the massive block of text into smaller "chunks". However, you cannot split a chunk in the middle of a sentence.
The Task:
Write a function that takes a long string of text and an integer max_chars.

Split the text into sentences (you can assume sentences only end with a period followed by a space: ". ").

Group the sentences together into chunks. A chunk should contain as many sentences as possible without exceeding max_chars.

If a single sentence is longer than max_chars all by itself, you have to break the rule and force-split it at exactly max_chars.

Output: Return a list of strings, where each string is a properly sized chunk.
"""

"""
The Context-Aware Text Chunker
Concepts: String parsing, boundary conditions, building accumulators.
The Premise: You are preparing a raw corporate earnings transcript to be fed into a Large Language Model. The LLM has a strict token limit, so you need to split the massive block of text into smaller "chunks". However, you cannot split a chunk in the middle of a sentence.
The Task:
Write a function that takes a long string of text and an integer max_chars.

Split the text into sentences (you can assume sentences only end with a period followed by a space: ". ").

Group the sentences together into chunks. A chunk should contain as many sentences as possible without exceeding max_chars.

If a single sentence is longer than max_chars all by itself, you have to break the rule and force-split it at exactly max_chars.

Output: Return a list of strings, where each string is a properly sized chunk.
"""
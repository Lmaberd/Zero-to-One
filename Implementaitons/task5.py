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
text  = ("Oil markets rallied sharply on Monday after US-Iran talks collapsed over the weekend. ICE Brent jumped more than 9% in early trade, while NYMEX WTI pushed above $105/bbl. In response, the US military plans to implement a blockade of all maritime traffic entering and exiting Iranian ports from 10:00am Monday Washington time, while allowing vessels not calling at Iranian ports to continue transiting Hormuz. Despite this, two fuel tankers attempted to exit the Gulf via routes close to Iran’s coastline, marking the first such movements since the blockade was announced.")

def chunker(text, max_chars):
    sentence = text.split(". ")
    chunks = []
    current = ""

    for s in sentence:
        if len(s) > max_chars:

            # Flush temporary string to final chunk
            if len(current) != 0:
                chunks.append(current)
                current = ""
            
            # Append up to max_chars and store remaining chars in temporary string
            chunks.append(s[:max_chars+1])
            current = s[max_chars:] + ". "
        
        elif len(current) + len(s) > max_chars:
            if len(current) < max_chars:
                chunks.append(current)
            
            if len(s) > max_chars(s):
                chunks.append(s[:max_chars+1])
                current = s[max_chars:] + ". "
        
        else:
            chunks.append(s)
    
    if len(current) > 0:
        chunks.append(current)

    return chunks

print(chunker(text, 5000))







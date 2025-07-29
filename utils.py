import math

def calculate_entropy(data):
    if not data:
        return 0
    freq = {}
    for b in data:
        freq[b] = freq.get(b, 0) + 1

    entropy = 0
    for f in freq.values():
        p = f / len(data)
        entropy -= p * math.log2(p)
    return entropy

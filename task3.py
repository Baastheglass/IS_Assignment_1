import re
from collections import Counter
import matplotlib.pyplot as plt

with open("ciphertext.txt", "r") as f:
    ciphertext = f.read()

# regex pattern for homophone tokens
pattern = re.compile(r"[a-z]\d+")

# extracting valid trigrams
trigrams = []
prev1, prev2 = None, None
prev_end1, prev_end2 = None, None

for match in pattern.finditer(ciphertext):
    token = match.group()
    start, end = match.span()

    # if previous two tokens were consecutive and this one is also consecutive
    if prev1 and prev2 and prev_end2 == start - 1 and prev_end1 == prev_start2 - 1:
        trigrams.append(f"{prev1}-{prev2}-{token}")

    # shift tokens
    prev1, prev2 = prev2, token
    prev_start1, prev_start2 = prev_end1, start
    prev_end1, prev_end2 = prev_end2, end

# counting trigram frequencies
trigram_counts = Counter(trigrams)

# getting top 10
top_trigrams = trigram_counts.most_common(10)

# plotting bar graph
if top_trigrams:
    labels, counts = zip(*top_trigrams)
    plt.figure(figsize=(10, 6))
    plt.bar(labels, counts)
    plt.xticks(rotation=45, ha="right")
    plt.title("Top 10 Trigram Frequencies in Ciphertext")
    plt.xlabel("Trigram")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()
else:
    print("No valid trigrams found.")
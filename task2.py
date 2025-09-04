import re
from collections import Counter
import matplotlib.pyplot as plt

with open("ciphertext.txt", "r") as f:
    ciphertext = f.read()


# regex pattern for homophone tokens
pattern = re.compile(r"[a-z]\d+")

# extracting valid bigrams
bigrams = []
prev_token, prev_end = None, None
for match in pattern.finditer(ciphertext):
    token = match.group()
    start, end = match.span()
    # only form bigram if tokens are consecutive with '|' between them
    if prev_token and prev_end == start - 1:
        bigrams.append(f"{prev_token}-{token}")
    prev_token, prev_end = token, end

# counting bigram frequencies
bigram_counts = Counter(bigrams)

# getting top 15
top_bigrams = bigram_counts.most_common(15)

# plotting bar graph
labels, counts = zip(*top_bigrams)
plt.figure(figsize=(10, 6))
plt.bar(labels, counts)
plt.xticks(rotation=45, ha="right")
plt.title("Top 15 Bigram Frequencies in Ciphertext")
plt.xlabel("Bigram")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

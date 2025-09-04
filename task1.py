import re
from collections import Counter
import matplotlib.pyplot as plt

with open("ciphertext.txt", "r") as f:
    ciphertext = f.read()
# Step 1: extract tokens (things like e8, o8, b3, etc.)
tokens = re.findall(r"[a-z]\d+", ciphertext)

# Step 2: count frequencies
freq = Counter(tokens)

sorted_freq = freq.most_common()

# Show results
for token, count in sorted_freq:
    print(f"{token}: {count}")

# Step 3: plot frequencies
tokens, counts = zip(*sorted_freq)
plt.bar(tokens, counts)
plt.xlabel("Tokens")
plt.ylabel("Frequencies")
plt.title("Token Frequencies in Ciphertext")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


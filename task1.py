import re
from collections import Counter
import matplotlib.pyplot as plt

with open("ciphertext.txt", "r") as f:
    ciphertext = f.read()
# extracting tokens (things like e8, o8, b3, etc.)
tokens = re.findall(r"[a-z]\d+", ciphertext)

# counting frequencies
freq = Counter(tokens)

sorted_freq = freq.most_common()

# show results
for token, count in sorted_freq:
    print(f"{token}: {count}")

# plotting frequencies
tokens, counts = zip(*sorted_freq)
plt.bar(tokens, counts)
plt.xlabel("Tokens")
plt.ylabel("Frequencies")
plt.title("Token Frequencies in Ciphertext")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


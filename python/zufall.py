# Erzeugt mit ChatGPT 5
#
# Prompt: Create a column graph in text for the probability
# of the outcome of 3 dices in python

from collections import Counter
import itertools

# Calculate probabilities for 3 dice
dice = [1, 2, 3, 4, 5, 6]
sums = [sum(roll) for roll in itertools.product(dice, repeat=3)]
counts = Counter(sums)

# Normalize to probabilities
total = len(sums)
probs = {s: counts[s]/total for s in range(3, 19)}  # possible sums from 3 to 18

# Scale probabilities to fit column graph height
max_height = 20
scale = max_height / max(probs.values())

# Draw the column graph
print("Probability distribution of 3 dice (text column graph)\n")
for level in range(max_height, 0, -1):  # top to bottom
    line = ""
    for s in range(3, 19):
        if probs[s] * scale >= level:
            line += "█ "   # block character for column
        else:
            line += "  "
    print(line)

# Print labels at the bottom
print(" ".join(f"{s:2}" for s in range(3, 19)))

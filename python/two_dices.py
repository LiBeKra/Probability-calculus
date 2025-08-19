import matplotlib.pyplot as plt
from collections import Counter
import itertools

# Step 1: Simulate all possible outcomes of rolling two dice
dice_faces = range(1, 7)
outcomes = list(itertools.product(dice_faces, repeat=2))
sums = [sum(outcome) for outcome in outcomes]

# Step 2: Count frequency of each sum
sum_counts = Counter(sums)
total_outcomes = len(outcomes)
probabilities = {k: v / total_outcomes for k, v in sum_counts.items()}

# Step 3: Plot the probabilities
plt.figure(figsize=(10, 6))
plt.bar(probabilities.keys(), probabilities.values(), color='skyblue', edgecolor='black')
plt.title('Probability Distribution of Sum of Two Dice', fontsize=14)
plt.xlabel('Sum of Dice', fontsize=12)
plt.ylabel('Probability', fontsize=12)
plt.xticks(range(2, 13))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

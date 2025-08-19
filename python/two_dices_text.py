from collections import Counter
import itertools

# Step 1: Generate all possible outcomes
dice_faces = range(1, 7)
outcomes = list(itertools.product(dice_faces, repeat=2))
sums = [sum(outcome) for outcome in outcomes]

# Step 2: Count frequency of each sum
sum_counts = Counter(sums)
total_outcomes = len(outcomes)

# Step 3: Display probabilities as a text-based bar chart
print("Probability Distribution of Sum of Two Dice:\n")
for total in range(2, 13):
    count = sum_counts[total]
    probability = count / total_outcomes
    bar = '█' * int(probability * 100)  # scale bar length
    print(f"{total:2} | {bar} {probability:.2%}")
